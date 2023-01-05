from lsprotocol.types import (TEXT_DOCUMENT_COMPLETION, TEXT_DOCUMENT_DID_CHANGE,
                               TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN,
                               TEXT_DOCUMENT_HOVER,
                               TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL,
                               TEXT_DOCUMENT_DEFINITION)
from lsprotocol.types import (CompletionItem, CompletionList, CompletionOptions,
                             CompletionParams, ConfigurationItem,
                             ConfigurationParams, Diagnostic,
                             DidChangeTextDocumentParams,
                             DidCloseTextDocumentParams,
                             DidOpenTextDocumentParams, MessageType, Position,
                             Range, Registration, RegistrationParams,
                             SemanticTokens, SemanticTokensLegend, SemanticTokensParams,
                             Unregistration, UnregistrationParams,
                             WorkDoneProgressBegin, WorkDoneProgressEnd,
                             WorkDoneProgressReport,
                             Hover,HoverOptions,
                             Definition, DefinitionOptions,DefinitionParams,
                             Range, Location, LocationLink
)
from pygls.server import LanguageServer

import antlr4
from server.ttcn3Visitor import ttcn3Visitor
from server.ttcn3Parser import ttcn3Parser
from server.ttcn3Lexer import ttcn3Lexer
import logging
import uuid
import asyncio

logger = logging.getLogger(__name__)


# Why can't I import ttcn3Visitor??
# re-generate to fit this version of python3.8-antlr4-runtime..?
class Visitor(ttcn3Visitor):
    # we don't care about scopes we're FREAKS!
    # Structure of symbol table dict:
    # filename:
    #   stream --> stream
    #   functionnName (string)
    #       line, column (list of integers)
    def __init__(self,filename,stream):
        self.filename = filename
        self.symbolTable = dict()
        self.symbolTable[self.filename] = dict()
        self.symbolTable[self.filename]["stream"] = stream

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

# Init server

class ttcn3LanguageServer(LanguageServer):
    CMD_RESTART_SERVER = 'restart_server'
    CONFIGURATION_SECTION = 'ttcn3Server'

    def __init__(self, *args):
        super().__init__(*args)
        self.symbolTable = dict()
        # Run lexer and parser on each file
        self.filenames = ['/home/johan/ttcn/ttcn3-vscode-lsp/test.ttcn', '/home/johan/ttcn/ttcn3-vscode-lsp/test2.ttcn']
        for filename in self.filenames:
            inputStream = antlr4.FileStream(filename);
            lexer = ttcn3Lexer(inputStream)
            stream = antlr4.CommonTokenStream(lexer)
            parser = ttcn3Parser(stream)
            tree = parser.ttcn3module()
            visitor = Visitor(filename,stream)
            visitor.visitTtcn3module(tree)
            # Add local current symbol table to global symbol table
            self.symbolTable = {**visitor.symbolTable,**self.symbolTable}



ttcn_server = ttcn3LanguageServer('ccls-for-ttcn3', 'v2.0')





@ttcn_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(server: ttcn3LanguageServer, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    # re-run parser?

@ttcn_server.feature(TEXT_DOCUMENT_DEFINITION,DefinitionOptions())
def jonas2(server: ttcn3LanguageServer, params: DefinitionParams):
            # use params.text_document and params.position to figure out where to send client
            # Want to find definition for token at line Y column X
            # loop over each token in current file to find what token we have at Y:X
            # "position":{"line":11,"character":12}}
            uri       = params.text_document.uri.split("file://")[1]
            # line counts offset from zero!
            line      = params.position.line+1
            character = params.position.character

            # Start looping through files.
            # This is retared probably, I need to use scopes
            # and travel one scope upwards at a time
            logger.debug(server.symbolTable)
            # logger.debug("filename = %s", filename)
            # logger.debug("uri.split(\"/\")[-1] = %s",uri.split("/")[-1])

            # Check for each file if that symbol table has symbol by that name and position

            # Check if we have indexed this file at all
            if uri in server.symbolTable.keys():
                logger.debug("uri found in symbol table")
                # Now check what token we have at that position
                stream = server.symbolTable[uri]["stream"]
                # stream is not iterable :(
                for i in range(0,len(stream.tokens)):
                    token = stream.get(i)
                    # Stop when we're at the correct position
                    # and check if we have that function defined in any local symbol table
                    logger.debug("token.line=%i",token.line)
                    logger.debug("line=%i",line)
                    logger.debug("character=%i",character)
                    logger.debug(range(token.column+1,(token.stop-token.start)+token.column+3))
                    if token.line == line and (character in range(token.column+1,(token.stop-token.start)+token.column+3)):
                        logger.debug("token.line found in file")
                        logger.debug("token.text=%s",token.text)
                        for key in server.symbolTable:
                            logger.debug("server.symbolTable[key].keys()=%s",server.symbolTable[key].keys())
                            if token.text in server.symbolTable[key].keys():
                                def_line = server.symbolTable[key][token.text][0]-1
                                def_column = server.symbolTable[key][token.text][1]
                                location = Location(uri="file://"+key,
                                                    range=Range(start=Position(def_line, def_column),end=Position(line=def_line, character=def_column),),)
                                return location

@ttcn_server.feature(TEXT_DOCUMENT_HOVER,HoverOptions())
def jonas(server: ttcn3LanguageServer, params):
    # return Hover("hej")
    return None


@ttcn_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def did_close(server: ttcn3LanguageServer, params: DidCloseTextDocumentParams):
    """Text document did close notification."""


@ttcn_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""


@ttcn_server.command(ttcn3LanguageServer.CMD_RESTART_SERVER)
def restart_server(ls: ttcn3LanguageServer, *args):
    ls.progress().create()
    ls.show_message('beep bop bop')
