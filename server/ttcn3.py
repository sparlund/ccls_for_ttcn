import antlr4
from ttcn3Lexer import ttcn3Lexer
from ttcn3Listener import ttcn3Listener
from ttcn3Visitor import ttcn3Visitor
from ttcn3Parser import ttcn3Parser
import json


class Context:
    def __init__(self):
        pass

class Module(Context):
    def __init__(self, name):
        self.name = name

class Function(Context):
    def __init__(self, name):
        self.name = name


class tl(ttcn3Listener):
    def __init__(self):
        self.context = []
    # def enterTtcn3moduleId(self, ctx:ttcn3Parser.Ttcn3moduleContext):
        # print(ctx.getSourceInterval())
        # print(ctx.getPayload())
    def enterModuleId(self, ctx:ttcn3Parser.ModuleIdContext):
        self.context.append(Module(ctx.getChild(0).getText()))
    def exitModuleId(self, ctx:ttcn3Parser.ModuleIdContext):
        # Leaving module, set context blank
        self.context = None
    # function definition
    # def enterFunctionDef(self, ctx:ttcn3Parser.FunctionDefContext):

    #     self.data[str(ctx.getChild(0).getSymbol().line)+":"+str(ctx.getChild(0).getSymbol().column)] = ctx.getChild(0).getParent()
    def enterCommonDef(self, ctx:ttcn3Parser.CommonDefContext):
        print(ctx.getChild(0).getTokens(ttcn3Parser.INTEGER))

    # function statement is execution of function?
    # def enterFunctionStatementList(self, ctx:ttcn3Parser.FunctionStatementListContext):
    #     for i in ctx.getChildren():
    #         try:
    #             print(i.getSymbol().line)
    #             print(i.getSymbol().column)
    #             print("--")
    #         except:
    #   load          pass
    # def exitFunctionStatementList(self, ctx:ttcn3Parser.FunctionStatementListContext):
    #     for i in ctx.getChildren():
    #         try:
    #             print(i.getSymbol().line)
    #             print(i.getSymbol().column)
    #         except:
    #             pass

#     def enterConstDef(self, ctx:ttcn3Parser.SingleConstDefContext):
#         print("a")
#         print(ctx.getText())
#         pass


#     def enterIntegervalue(self, ctx:ttcn3Parser.IntegervalueContext):
#         # print(ctx.getPayload())
#         pass

#     def exitIntegervalue(self, ctx:ttcn3Parser.IntegervalueContext):
#         # print(ctx.getPayload())
#         pass


#     def exitModuleId(self, ctx:ttcn3Parser.ModuleIdContext):
#         # print(ctx.getT)
#         # for i in 
#         pass


class Visitor(ttcn3Visitor):
    # we don't care about scopes we're FREAKS!
    # Structure of symbol table dict:
    # filename:
    #   functionnName (string)
    #       line, column (list of integers)
    symbolTable = dict()
    def __init__(self,filename):
        self.filename = filename
        self.symbolTable[self.filename] = dict()

    def visitTtcn3module(self, ctx:ttcn3Parser.Ttcn3moduleContext):
        # Visit and save current module name
        # self.visitModuleId(ctx.getChild(1))
        self.visitModuleDefinitionsList(ctx.getChild(3))
        return 0

    def visitModuleId(self, ctx:ttcn3Parser.ModuleIdContext):
        # maybe todo: introduce scope concept
        self.current_moduleId = ctx.getText()

    def visitModuleDefinitionsList(self, ctx:ttcn3Parser.ModuleDefinitionsListContext):
        # print("in visitModuleDefinitionsList: type(ctx)=",type(ctx))
        for i in range(0,ctx.getChildCount()):
            # print("in visitModuleDefinitionsList: type(ctx.getChild("+str(i)+"))=",type(ctx.getChild(i)))
            self.visitModuleDefinition(ctx.getChild(i))

    def visitModuleDefinition(self, ctx:ttcn3Parser.ModuleDefinitionContext):
        for i in range(0,ctx.getChildCount()):
                self.visitCommonDef(ctx.getChild(i))

    def visitCommonDef(self, ctx:ttcn3Parser.CommonDefContext):
        # print("in visitCommonDef: type(ctx)=",type(ctx))
        for i in range(0, ctx.getChildCount()):
            # print("in visitCommonDef: type(ctx.getChild("+str(i)+"))",type(ctx.getChild(i)))
            if isinstance(ctx.getChild(i),ttcn3Parser.FunctionDefContext):
                self.visitFunctionDef(ctx.getChild(i))

    # # Besök ALLA noder ner till functionDef???
    def visitFunctionDef(self, ctx:ttcn3Parser.FunctionDefContext):
        self.symbolTable[self.filename][ctx.getChild(1).getText()] = [ctx.getChild(1).getSymbol().line,ctx.getChild(1).getSymbol().column+1]

filename = '../test.ttcn'
inputStream = antlr4.FileStream(filename);
lexer = ttcn3Lexer(inputStream)
stream = antlr4.CommonTokenStream(lexer)
parser = ttcn3Parser(stream)
tree = parser.ttcn3module()
visitor = Visitor(filename)
visitor.visitTtcn3module(tree)

# Want to find definition for token at line 31 column 14 --> func_func4 is correct answer
# loop over each token in current file to find what token we have at 31:14
# We will get 31:14 and a filename as parameter from client message
for i in range(0,len(stream.tokens)):
    # this token is defined from token.column+1 to (token.stop-token.start)+token.column+2
    token = stream.get(i)
    if token.line == 31 and (14 in range(token.column+1,(token.stop-token.start)+token.column+3)):
        break
# Now let's find this token inside our symbol table
print("token found at:", visitor.symbolTable[filename][token.text])


print(json.dumps(visitor.symbolTable,indent=2))



# print(tree.toStringTree(recog=parser))
# listener = tl()
# tl.filename = "test.ttcn"







