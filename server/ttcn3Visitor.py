# Generated from ttcn3.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ttcn3Parser import ttcn3Parser
else:
    from ttcn3Parser import ttcn3Parser

# This class defines a complete generic visitor for a parse tree produced by ttcn3Parser.

class ttcn3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by ttcn3Parser#ttcn3module.
    def visitTtcn3module(self, ctx:ttcn3Parser.Ttcn3moduleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ttcn3Parser#moduleId.
    def visitModuleId(self, ctx:ttcn3Parser.ModuleIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#languageSpec.
    def visitLanguageSpec(self, ctx:ttcn3Parser.LanguageSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#moduleDefinitionsList.
    def visitModuleDefinitionsList(self, ctx:ttcn3Parser.ModuleDefinitionsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#moduleDefinition.
    def visitModuleDefinition(self, ctx:ttcn3Parser.ModuleDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#commonDef.
    def visitCommonDef(self, ctx:ttcn3Parser.CommonDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#visibility.
    def visitVisibility(self, ctx:ttcn3Parser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#typeDef.
    def visitTypeDef(self, ctx:ttcn3Parser.TypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#typeDefBody.
    def visitTypeDefBody(self, ctx:ttcn3Parser.TypeDefBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#structuredTypeDef.
    def visitStructuredTypeDef(self, ctx:ttcn3Parser.StructuredTypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#recordDef.
    def visitRecordDef(self, ctx:ttcn3Parser.RecordDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#structDefBody.
    def visitStructDefBody(self, ctx:ttcn3Parser.StructDefBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#structFieldDef.
    def visitStructFieldDef(self, ctx:ttcn3Parser.StructFieldDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedTypeDef.
    def visitNestedTypeDef(self, ctx:ttcn3Parser.NestedTypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedRecordDef.
    def visitNestedRecordDef(self, ctx:ttcn3Parser.NestedRecordDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedUnionDef.
    def visitNestedUnionDef(self, ctx:ttcn3Parser.NestedUnionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedSetDef.
    def visitNestedSetDef(self, ctx:ttcn3Parser.NestedSetDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedRecordOfDef.
    def visitNestedRecordOfDef(self, ctx:ttcn3Parser.NestedRecordOfDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedSetOfDef.
    def visitNestedSetOfDef(self, ctx:ttcn3Parser.NestedSetOfDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#nestedEnumDef.
    def visitNestedEnumDef(self, ctx:ttcn3Parser.NestedEnumDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#unionDef.
    def visitUnionDef(self, ctx:ttcn3Parser.UnionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#unionDefBody.
    def visitUnionDefBody(self, ctx:ttcn3Parser.UnionDefBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#unionFieldDef.
    def visitUnionFieldDef(self, ctx:ttcn3Parser.UnionFieldDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#setDef.
    def visitSetDef(self, ctx:ttcn3Parser.SetDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#recordOfDef.
    def visitRecordOfDef(self, ctx:ttcn3Parser.RecordOfDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#structOfDefBody.
    def visitStructOfDefBody(self, ctx:ttcn3Parser.StructOfDefBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#setOfDef.
    def visitSetOfDef(self, ctx:ttcn3Parser.SetOfDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#enumDef.
    def visitEnumDef(self, ctx:ttcn3Parser.EnumDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#enumerationList.
    def visitEnumerationList(self, ctx:ttcn3Parser.EnumerationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#enumeration.
    def visitEnumeration(self, ctx:ttcn3Parser.EnumerationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#integerValueOrRange.
    def visitIntegerValueOrRange(self, ctx:ttcn3Parser.IntegerValueOrRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#subTypeDef.
    def visitSubTypeDef(self, ctx:ttcn3Parser.SubTypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#subTypeSpec.
    def visitSubTypeSpec(self, ctx:ttcn3Parser.SubTypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allowedValuesSpec.
    def visitAllowedValuesSpec(self, ctx:ttcn3Parser.AllowedValuesSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateOrRange.
    def visitTemplateOrRange(self, ctx:ttcn3Parser.TemplateOrRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#stringLength.
    def visitStringLength(self, ctx:ttcn3Parser.StringLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portDef.
    def visitPortDef(self, ctx:ttcn3Parser.PortDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portDefAttribs.
    def visitPortDefAttribs(self, ctx:ttcn3Parser.PortDefAttribsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#messageAttribs.
    def visitMessageAttribs(self, ctx:ttcn3Parser.MessageAttribsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#configParamDef.
    def visitConfigParamDef(self, ctx:ttcn3Parser.ConfigParamDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#addressDecl.
    def visitAddressDecl(self, ctx:ttcn3Parser.AddressDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#messageList.
    def visitMessageList(self, ctx:ttcn3Parser.MessageListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allOrTypeList.
    def visitAllOrTypeList(self, ctx:ttcn3Parser.AllOrTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#typeList.
    def visitTypeList(self, ctx:ttcn3Parser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#procedureAttribs.
    def visitProcedureAttribs(self, ctx:ttcn3Parser.ProcedureAttribsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#procedureList.
    def visitProcedureList(self, ctx:ttcn3Parser.ProcedureListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allOrSignatureList.
    def visitAllOrSignatureList(self, ctx:ttcn3Parser.AllOrSignatureListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#signatureList.
    def visitSignatureList(self, ctx:ttcn3Parser.SignatureListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#mixedAttribs.
    def visitMixedAttribs(self, ctx:ttcn3Parser.MixedAttribsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#mixedList.
    def visitMixedList(self, ctx:ttcn3Parser.MixedListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#procOrTypeList.
    def visitProcOrTypeList(self, ctx:ttcn3Parser.ProcOrTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#procOrType.
    def visitProcOrType(self, ctx:ttcn3Parser.ProcOrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentDef.
    def visitComponentDef(self, ctx:ttcn3Parser.ComponentDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentType.
    def visitComponentType(self, ctx:ttcn3Parser.ComponentTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentDefList.
    def visitComponentDefList(self, ctx:ttcn3Parser.ComponentDefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentElementDef.
    def visitComponentElementDef(self, ctx:ttcn3Parser.ComponentElementDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portInstance.
    def visitPortInstance(self, ctx:ttcn3Parser.PortInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portElement.
    def visitPortElement(self, ctx:ttcn3Parser.PortElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#constDef.
    def visitConstDef(self, ctx:ttcn3Parser.ConstDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#constList.
    def visitConstList(self, ctx:ttcn3Parser.ConstListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleConstDef.
    def visitSingleConstDef(self, ctx:ttcn3Parser.SingleConstDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateDef.
    def visitTemplateDef(self, ctx:ttcn3Parser.TemplateDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#baseTemplate.
    def visitBaseTemplate(self, ctx:ttcn3Parser.BaseTemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateOrValueFormalParList.
    def visitTemplateOrValueFormalParList(self, ctx:ttcn3Parser.TemplateOrValueFormalParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateOrValueFormalPar.
    def visitTemplateOrValueFormalPar(self, ctx:ttcn3Parser.TemplateOrValueFormalParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateBody.
    def visitTemplateBody(self, ctx:ttcn3Parser.TemplateBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#simpleSpec.
    def visitSimpleSpec(self, ctx:ttcn3Parser.SimpleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#simpleTemplateSpec.
    def visitSimpleTemplateSpec(self, ctx:ttcn3Parser.SimpleTemplateSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleTemplateExpression.
    def visitSingleTemplateExpression(self, ctx:ttcn3Parser.SingleTemplateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#enumTemplateExtension.
    def visitEnumTemplateExtension(self, ctx:ttcn3Parser.EnumTemplateExtensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldSpecList.
    def visitFieldSpecList(self, ctx:ttcn3Parser.FieldSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldSpec.
    def visitFieldSpec(self, ctx:ttcn3Parser.FieldSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldReference.
    def visitFieldReference(self, ctx:ttcn3Parser.FieldReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayOrBitRef.
    def visitArrayOrBitRef(self, ctx:ttcn3Parser.ArrayOrBitRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayValueOrAttrib.
    def visitArrayValueOrAttrib(self, ctx:ttcn3Parser.ArrayValueOrAttribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayElementSpec.
    def visitArrayElementSpec(self, ctx:ttcn3Parser.ArrayElementSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#matchingSymbol.
    def visitMatchingSymbol(self, ctx:ttcn3Parser.MatchingSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#decodedContentMatch.
    def visitDecodedContentMatch(self, ctx:ttcn3Parser.DecodedContentMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#extraMatchingAttributes.
    def visitExtraMatchingAttributes(self, ctx:ttcn3Parser.ExtraMatchingAttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#charStringMatch.
    def visitCharStringMatch(self, ctx:ttcn3Parser.CharStringMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#patternParticle.
    def visitPatternParticle(self, ctx:ttcn3Parser.PatternParticleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#pattern.
    def visitPattern(self, ctx:ttcn3Parser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#escPattern.
    def visitEscPattern(self, ctx:ttcn3Parser.EscPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#concate.
    def visitConcate(self, ctx:ttcn3Parser.ConcateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#patternElement.
    def visitPatternElement(self, ctx:ttcn3Parser.PatternElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#patternChar.
    def visitPatternChar(self, ctx:ttcn3Parser.PatternCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#patternClassChar.
    def visitPatternClassChar(self, ctx:ttcn3Parser.PatternClassCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#complement.
    def visitComplement(self, ctx:ttcn3Parser.ComplementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#listOfTemplates.
    def visitListOfTemplates(self, ctx:ttcn3Parser.ListOfTemplatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateListItem.
    def visitTemplateListItem(self, ctx:ttcn3Parser.TemplateListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#subsetMatch.
    def visitSubsetMatch(self, ctx:ttcn3Parser.SubsetMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#supersetMatch.
    def visitSupersetMatch(self, ctx:ttcn3Parser.SupersetMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#permutationMatch.
    def visitPermutationMatch(self, ctx:ttcn3Parser.PermutationMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#wildcardLengthMatch.
    def visitWildcardLengthMatch(self, ctx:ttcn3Parser.WildcardLengthMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#bound.
    def visitBound(self, ctx:ttcn3Parser.BoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#actualParAssignment.
    def visitActualParAssignment(self, ctx:ttcn3Parser.ActualParAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateRefWithParList.
    def visitTemplateRefWithParList(self, ctx:ttcn3Parser.TemplateRefWithParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateInstance.
    def visitTemplateInstance(self, ctx:ttcn3Parser.TemplateInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#actualParList.
    def visitActualParList(self, ctx:ttcn3Parser.ActualParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#actualPar.
    def visitActualPar(self, ctx:ttcn3Parser.ActualParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateOps.
    def visitTemplateOps(self, ctx:ttcn3Parser.TemplateOpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionDef.
    def visitFunctionDef(self, ctx:ttcn3Parser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionFormalParList.
    def visitFunctionFormalParList(self, ctx:ttcn3Parser.FunctionFormalParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionFormalPar.
    def visitFunctionFormalPar(self, ctx:ttcn3Parser.FunctionFormalParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#returnType.
    def visitReturnType(self, ctx:ttcn3Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#runsOnSpec.
    def visitRunsOnSpec(self, ctx:ttcn3Parser.RunsOnSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#mtcSpec.
    def visitMtcSpec(self, ctx:ttcn3Parser.MtcSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#statementBlock.
    def visitStatementBlock(self, ctx:ttcn3Parser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionDefList.
    def visitFunctionDefList(self, ctx:ttcn3Parser.FunctionDefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionStatementList.
    def visitFunctionStatementList(self, ctx:ttcn3Parser.FunctionStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionLocalInst.
    def visitFunctionLocalInst(self, ctx:ttcn3Parser.FunctionLocalInstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionLocalDef.
    def visitFunctionLocalDef(self, ctx:ttcn3Parser.FunctionLocalDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionStatement.
    def visitFunctionStatement(self, ctx:ttcn3Parser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#functionInstance.
    def visitFunctionInstance(self, ctx:ttcn3Parser.FunctionInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#signatureDef.
    def visitSignatureDef(self, ctx:ttcn3Parser.SignatureDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#signatureFormalParList.
    def visitSignatureFormalParList(self, ctx:ttcn3Parser.SignatureFormalParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#signature.
    def visitSignature(self, ctx:ttcn3Parser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#testcaseDef.
    def visitTestcaseDef(self, ctx:ttcn3Parser.TestcaseDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#systemSpec.
    def visitSystemSpec(self, ctx:ttcn3Parser.SystemSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#testcaseInstance.
    def visitTestcaseInstance(self, ctx:ttcn3Parser.TestcaseInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#altstepDef.
    def visitAltstepDef(self, ctx:ttcn3Parser.AltstepDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#altstepLocalDefList.
    def visitAltstepLocalDefList(self, ctx:ttcn3Parser.AltstepLocalDefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#altstepLocalDef.
    def visitAltstepLocalDef(self, ctx:ttcn3Parser.AltstepLocalDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#altstepInstance.
    def visitAltstepInstance(self, ctx:ttcn3Parser.AltstepInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#importDef.
    def visitImportDef(self, ctx:ttcn3Parser.ImportDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#exceptsDef.
    def visitExceptsDef(self, ctx:ttcn3Parser.ExceptsDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#exceptElement.
    def visitExceptElement(self, ctx:ttcn3Parser.ExceptElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#identifierListOrAll.
    def visitIdentifierListOrAll(self, ctx:ttcn3Parser.IdentifierListOrAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#importElement.
    def visitImportElement(self, ctx:ttcn3Parser.ImportElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#groupRefListWithExcept.
    def visitGroupRefListWithExcept(self, ctx:ttcn3Parser.GroupRefListWithExceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allGroupsWithExcept.
    def visitAllGroupsWithExcept(self, ctx:ttcn3Parser.AllGroupsWithExceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#qualifiedIdentifierWithExcept.
    def visitQualifiedIdentifierWithExcept(self, ctx:ttcn3Parser.QualifiedIdentifierWithExceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#identifierListOrAllWithExcept.
    def visitIdentifierListOrAllWithExcept(self, ctx:ttcn3Parser.IdentifierListOrAllWithExceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allWithExcept.
    def visitAllWithExcept(self, ctx:ttcn3Parser.AllWithExceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#groupDef.
    def visitGroupDef(self, ctx:ttcn3Parser.GroupDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#extFunctionDef.
    def visitExtFunctionDef(self, ctx:ttcn3Parser.ExtFunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#extConstDef.
    def visitExtConstDef(self, ctx:ttcn3Parser.ExtConstDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#moduleParDef.
    def visitModuleParDef(self, ctx:ttcn3Parser.ModuleParDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#multitypedModuleParList.
    def visitMultitypedModuleParList(self, ctx:ttcn3Parser.MultitypedModuleParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#modulePar.
    def visitModulePar(self, ctx:ttcn3Parser.ModuleParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#moduleParList.
    def visitModuleParList(self, ctx:ttcn3Parser.ModuleParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#friendModuleDef.
    def visitFriendModuleDef(self, ctx:ttcn3Parser.FriendModuleDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#moduleControlPart.
    def visitModuleControlPart(self, ctx:ttcn3Parser.ModuleControlPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#moduleControlBody.
    def visitModuleControlBody(self, ctx:ttcn3Parser.ModuleControlBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#controlStatementOrDef.
    def visitControlStatementOrDef(self, ctx:ttcn3Parser.ControlStatementOrDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#varInstance.
    def visitVarInstance(self, ctx:ttcn3Parser.VarInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#varList.
    def visitVarList(self, ctx:ttcn3Parser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleVarInstance.
    def visitSingleVarInstance(self, ctx:ttcn3Parser.SingleVarInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#tempVarList.
    def visitTempVarList(self, ctx:ttcn3Parser.TempVarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleTempVarInstance.
    def visitSingleTempVarInstance(self, ctx:ttcn3Parser.SingleTempVarInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#variableRef.
    def visitVariableRef(self, ctx:ttcn3Parser.VariableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#timerInstance.
    def visitTimerInstance(self, ctx:ttcn3Parser.TimerInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayIdentifierRef.
    def visitArrayIdentifierRef(self, ctx:ttcn3Parser.ArrayIdentifierRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#configurationStatements.
    def visitConfigurationStatements(self, ctx:ttcn3Parser.ConfigurationStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#configurationOps.
    def visitConfigurationOps(self, ctx:ttcn3Parser.ConfigurationOpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#createOp.
    def visitCreateOp(self, ctx:ttcn3Parser.CreateOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#doneStatement.
    def visitDoneStatement(self, ctx:ttcn3Parser.DoneStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentOrAny.
    def visitComponentOrAny(self, ctx:ttcn3Parser.ComponentOrAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#valueStoreSpec.
    def visitValueStoreSpec(self, ctx:ttcn3Parser.ValueStoreSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#indexAssignment.
    def visitIndexAssignment(self, ctx:ttcn3Parser.IndexAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#indexSpec.
    def visitIndexSpec(self, ctx:ttcn3Parser.IndexSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#killedStatement.
    def visitKilledStatement(self, ctx:ttcn3Parser.KilledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#runningOp.
    def visitRunningOp(self, ctx:ttcn3Parser.RunningOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#aliveOp.
    def visitAliveOp(self, ctx:ttcn3Parser.AliveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleConnectionSpec.
    def visitSingleConnectionSpec(self, ctx:ttcn3Parser.SingleConnectionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portRef.
    def visitPortRef(self, ctx:ttcn3Parser.PortRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentRef.
    def visitComponentRef(self, ctx:ttcn3Parser.ComponentRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allConnectionsSpec.
    def visitAllConnectionsSpec(self, ctx:ttcn3Parser.AllConnectionsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allPortsSpec.
    def visitAllPortsSpec(self, ctx:ttcn3Parser.AllPortsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allCompsAllPortsSpec.
    def visitAllCompsAllPortsSpec(self, ctx:ttcn3Parser.AllCompsAllPortsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#paramClause.
    def visitParamClause(self, ctx:ttcn3Parser.ParamClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentReferenceOrLiteral.
    def visitComponentReferenceOrLiteral(self, ctx:ttcn3Parser.ComponentReferenceOrLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#componentOrDefaultReference.
    def visitComponentOrDefaultReference(self, ctx:ttcn3Parser.ComponentOrDefaultReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#communicationStatements.
    def visitCommunicationStatements(self, ctx:ttcn3Parser.CommunicationStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#toClause.
    def visitToClause(self, ctx:ttcn3Parser.ToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#addressRefList.
    def visitAddressRefList(self, ctx:ttcn3Parser.AddressRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#callParameters.
    def visitCallParameters(self, ctx:ttcn3Parser.CallParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#callBodyStatement.
    def visitCallBodyStatement(self, ctx:ttcn3Parser.CallBodyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portOrAny.
    def visitPortOrAny(self, ctx:ttcn3Parser.PortOrAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portReceiveOp.
    def visitPortReceiveOp(self, ctx:ttcn3Parser.PortReceiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fromClause.
    def visitFromClause(self, ctx:ttcn3Parser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portRedirect.
    def visitPortRedirect(self, ctx:ttcn3Parser.PortRedirectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#valueSpec.
    def visitValueSpec(self, ctx:ttcn3Parser.ValueSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleValueSpec.
    def visitSingleValueSpec(self, ctx:ttcn3Parser.SingleValueSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#senderSpec.
    def visitSenderSpec(self, ctx:ttcn3Parser.SenderSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#triggerStatement.
    def visitTriggerStatement(self, ctx:ttcn3Parser.TriggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portTriggerOp.
    def visitPortTriggerOp(self, ctx:ttcn3Parser.PortTriggerOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#getCallStatement.
    def visitGetCallStatement(self, ctx:ttcn3Parser.GetCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portGetCallOp.
    def visitPortGetCallOp(self, ctx:ttcn3Parser.PortGetCallOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#redirectWithParamSpec.
    def visitRedirectWithParamSpec(self, ctx:ttcn3Parser.RedirectWithParamSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#paramSpec.
    def visitParamSpec(self, ctx:ttcn3Parser.ParamSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#paramAssignmentList.
    def visitParamAssignmentList(self, ctx:ttcn3Parser.ParamAssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#assignmentList.
    def visitAssignmentList(self, ctx:ttcn3Parser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#variableAssignment.
    def visitVariableAssignment(self, ctx:ttcn3Parser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#variableList.
    def visitVariableList(self, ctx:ttcn3Parser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#variableEntry.
    def visitVariableEntry(self, ctx:ttcn3Parser.VariableEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#getReplyStatement.
    def visitGetReplyStatement(self, ctx:ttcn3Parser.GetReplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portGetReplyOp.
    def visitPortGetReplyOp(self, ctx:ttcn3Parser.PortGetReplyOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#redirectWithValueAndParamSpec.
    def visitRedirectWithValueAndParamSpec(self, ctx:ttcn3Parser.RedirectWithValueAndParamSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#checkStatement.
    def visitCheckStatement(self, ctx:ttcn3Parser.CheckStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#checkParameter.
    def visitCheckParameter(self, ctx:ttcn3Parser.CheckParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fromClausePresent.
    def visitFromClausePresent(self, ctx:ttcn3Parser.FromClausePresentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#redirectPresent.
    def visitRedirectPresent(self, ctx:ttcn3Parser.RedirectPresentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#checkPortOpsPresent.
    def visitCheckPortOpsPresent(self, ctx:ttcn3Parser.CheckPortOpsPresentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#catchStatement.
    def visitCatchStatement(self, ctx:ttcn3Parser.CatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portCatchOp.
    def visitPortCatchOp(self, ctx:ttcn3Parser.PortCatchOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#catchOpParameter.
    def visitCatchOpParameter(self, ctx:ttcn3Parser.CatchOpParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#portOrAll.
    def visitPortOrAll(self, ctx:ttcn3Parser.PortOrAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#timerStatements.
    def visitTimerStatements(self, ctx:ttcn3Parser.TimerStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#timerOps.
    def visitTimerOps(self, ctx:ttcn3Parser.TimerOpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#timerRefOrAll.
    def visitTimerRefOrAll(self, ctx:ttcn3Parser.TimerRefOrAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#timeoutStatement.
    def visitTimeoutStatement(self, ctx:ttcn3Parser.TimeoutStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#timerRefOrAny.
    def visitTimerRefOrAny(self, ctx:ttcn3Parser.TimerRefOrAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#testcaseOperation.
    def visitTestcaseOperation(self, ctx:ttcn3Parser.TestcaseOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#type.
    def visitType(self, ctx:ttcn3Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#predefinedType.
    def visitPredefinedType(self, ctx:ttcn3Parser.PredefinedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#referencedType.
    def visitReferencedType(self, ctx:ttcn3Parser.ReferencedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#typeReference.
    def visitTypeReference(self, ctx:ttcn3Parser.TypeReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayDef.
    def visitArrayDef(self, ctx:ttcn3Parser.ArrayDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#value.
    def visitValue(self, ctx:ttcn3Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#predefinedValue.
    def visitPredefinedValue(self, ctx:ttcn3Parser.PredefinedValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#verdictValue.
    def visitVerdictValue(self, ctx:ttcn3Parser.VerdictValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#charStringValue.
    def visitCharStringValue(self, ctx:ttcn3Parser.CharStringValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#quadruple.
    def visitQuadruple(self, ctx:ttcn3Parser.QuadrupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#referencedValue.
    def visitReferencedValue(self, ctx:ttcn3Parser.ReferencedValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#formalValuePar.
    def visitFormalValuePar(self, ctx:ttcn3Parser.FormalValueParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#formalPortPar.
    def visitFormalPortPar(self, ctx:ttcn3Parser.FormalPortParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#formalTimerPar.
    def visitFormalTimerPar(self, ctx:ttcn3Parser.FormalTimerParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#formalTemplatePar.
    def visitFormalTemplatePar(self, ctx:ttcn3Parser.FormalTemplateParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#restrictedTemplate.
    def visitRestrictedTemplate(self, ctx:ttcn3Parser.RestrictedTemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#templateRestriction.
    def visitTemplateRestriction(self, ctx:ttcn3Parser.TemplateRestrictionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#withStatement.
    def visitWithStatement(self, ctx:ttcn3Parser.WithStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleWithAttrib.
    def visitSingleWithAttrib(self, ctx:ttcn3Parser.SingleWithAttribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#standardAttribute.
    def visitStandardAttribute(self, ctx:ttcn3Parser.StandardAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#variantAttribute.
    def visitVariantAttribute(self, ctx:ttcn3Parser.VariantAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#relatedEncoding.
    def visitRelatedEncoding(self, ctx:ttcn3Parser.RelatedEncodingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#attribKeyword.
    def visitAttribKeyword(self, ctx:ttcn3Parser.AttribKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#attribQualifier.
    def visitAttribQualifier(self, ctx:ttcn3Parser.AttribQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#defOrFieldRefList.
    def visitDefOrFieldRefList(self, ctx:ttcn3Parser.DefOrFieldRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#defOrFieldRef.
    def visitDefOrFieldRef(self, ctx:ttcn3Parser.DefOrFieldRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:ttcn3Parser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#allRef.
    def visitAllRef(self, ctx:ttcn3Parser.AllRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#behaviourStatements.
    def visitBehaviourStatements(self, ctx:ttcn3Parser.BehaviourStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#setLocalVerdict.
    def visitSetLocalVerdict(self, ctx:ttcn3Parser.SetLocalVerdictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#sutStatements.
    def visitSutStatements(self, ctx:ttcn3Parser.SutStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#altGuardList.
    def visitAltGuardList(self, ctx:ttcn3Parser.AltGuardListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#guardStatement.
    def visitGuardStatement(self, ctx:ttcn3Parser.GuardStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#altGuardChar.
    def visitAltGuardChar(self, ctx:ttcn3Parser.AltGuardCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#guardOp.
    def visitGuardOp(self, ctx:ttcn3Parser.GuardOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#interleavedGuardList.
    def visitInterleavedGuardList(self, ctx:ttcn3Parser.InterleavedGuardListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#activateOp.
    def visitActivateOp(self, ctx:ttcn3Parser.ActivateOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#basicStatements.
    def visitBasicStatements(self, ctx:ttcn3Parser.BasicStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#expression.
    def visitExpression(self, ctx:ttcn3Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#compoundExpression.
    def visitCompoundExpression(self, ctx:ttcn3Parser.CompoundExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldExpressionList.
    def visitFieldExpressionList(self, ctx:ttcn3Parser.FieldExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldExpressionSpec.
    def visitFieldExpressionSpec(self, ctx:ttcn3Parser.FieldExpressionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayExpression.
    def visitArrayExpression(self, ctx:ttcn3Parser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayElementExpressionList.
    def visitArrayElementExpressionList(self, ctx:ttcn3Parser.ArrayElementExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#notUsedOrExpression.
    def visitNotUsedOrExpression(self, ctx:ttcn3Parser.NotUsedOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#constantExpression.
    def visitConstantExpression(self, ctx:ttcn3Parser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#booleanExpression.
    def visitBooleanExpression(self, ctx:ttcn3Parser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#compoundConstExpression.
    def visitCompoundConstExpression(self, ctx:ttcn3Parser.CompoundConstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldConstExpressionList.
    def visitFieldConstExpressionList(self, ctx:ttcn3Parser.FieldConstExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#fieldConstExpressionSpec.
    def visitFieldConstExpressionSpec(self, ctx:ttcn3Parser.FieldConstExpressionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayConstExpression.
    def visitArrayConstExpression(self, ctx:ttcn3Parser.ArrayConstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#arrayElementConstExpressionList.
    def visitArrayElementConstExpressionList(self, ctx:ttcn3Parser.ArrayElementConstExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#assignment.
    def visitAssignment(self, ctx:ttcn3Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#singleExpression.
    def visitSingleExpression(self, ctx:ttcn3Parser.SingleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#xOrExpression.
    def visitXOrExpression(self, ctx:ttcn3Parser.XOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#andExpression.
    def visitAndExpression(self, ctx:ttcn3Parser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#notExpression.
    def visitNotExpression(self, ctx:ttcn3Parser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#equalExpression.
    def visitEqualExpression(self, ctx:ttcn3Parser.EqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#relExpression.
    def visitRelExpression(self, ctx:ttcn3Parser.RelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#shiftExpression.
    def visitShiftExpression(self, ctx:ttcn3Parser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#bitOrExpression.
    def visitBitOrExpression(self, ctx:ttcn3Parser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#bitXorExpression.
    def visitBitXorExpression(self, ctx:ttcn3Parser.BitXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#bitAndExpression.
    def visitBitAndExpression(self, ctx:ttcn3Parser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#bitNotExpression.
    def visitBitNotExpression(self, ctx:ttcn3Parser.BitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#addExpression.
    def visitAddExpression(self, ctx:ttcn3Parser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#mulExpression.
    def visitMulExpression(self, ctx:ttcn3Parser.MulExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:ttcn3Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#primary.
    def visitPrimary(self, ctx:ttcn3Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#extendedFieldReference.
    def visitExtendedFieldReference(self, ctx:ttcn3Parser.ExtendedFieldReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#decodedFieldType.
    def visitDecodedFieldType(self, ctx:ttcn3Parser.DecodedFieldTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#opCall.
    def visitOpCall(self, ctx:ttcn3Parser.OpCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#addOp.
    def visitAddOp(self, ctx:ttcn3Parser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#multiplyOp.
    def visitMultiplyOp(self, ctx:ttcn3Parser.MultiplyOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#unaryOp.
    def visitUnaryOp(self, ctx:ttcn3Parser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#relOp.
    def visitRelOp(self, ctx:ttcn3Parser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#equalOp.
    def visitEqualOp(self, ctx:ttcn3Parser.EqualOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#shiftOp.
    def visitShiftOp(self, ctx:ttcn3Parser.ShiftOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#logStatement.
    def visitLogStatement(self, ctx:ttcn3Parser.LogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#loopConstruct.
    def visitLoopConstruct(self, ctx:ttcn3Parser.LoopConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#initial.
    def visitInitial(self, ctx:ttcn3Parser.InitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#conditionalConstruct.
    def visitConditionalConstruct(self, ctx:ttcn3Parser.ConditionalConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#elseIfClause.
    def visitElseIfClause(self, ctx:ttcn3Parser.ElseIfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#elseClause.
    def visitElseClause(self, ctx:ttcn3Parser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#selectCaseConstruct.
    def visitSelectCaseConstruct(self, ctx:ttcn3Parser.SelectCaseConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#selectCaseBody.
    def visitSelectCaseBody(self, ctx:ttcn3Parser.SelectCaseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#selectCase.
    def visitSelectCase(self, ctx:ttcn3Parser.SelectCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#caseElse.
    def visitCaseElse(self, ctx:ttcn3Parser.CaseElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#extendedIdentifier.
    def visitExtendedIdentifier(self, ctx:ttcn3Parser.ExtendedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#identifierList.
    def visitIdentifierList(self, ctx:ttcn3Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#qualifiedIdentifierList.
    def visitQualifiedIdentifierList(self, ctx:ttcn3Parser.QualifiedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#getAttributeOp.
    def visitGetAttributeOp(self, ctx:ttcn3Parser.GetAttributeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#getAttributeSpec.
    def visitGetAttributeSpec(self, ctx:ttcn3Parser.GetAttributeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#logItem.
    def visitLogItem(self, ctx:ttcn3Parser.LogItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#actionText.
    def visitActionText(self, ctx:ttcn3Parser.ActionTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#booleanValue.
    def visitBooleanValue(self, ctx:ttcn3Parser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#freeText.
    def visitFreeText(self, ctx:ttcn3Parser.FreeTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#bitStringMatch.
    def visitBitStringMatch(self, ctx:ttcn3Parser.BitStringMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#hexStringMatch.
    def visitHexStringMatch(self, ctx:ttcn3Parser.HexStringMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#octStringMatch.
    def visitOctStringMatch(self, ctx:ttcn3Parser.OctStringMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ttcn3Parser#integervalue.
    def visitIntegervalue(self, ctx:ttcn3Parser.IntegervalueContext):
        return self.visitChildren(ctx)



del ttcn3Parser