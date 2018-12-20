# Generated from miniJavaExpr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# This class defines a complete listener for a parse tree produced by miniJavaExprParser.
class miniJavaExprListener(ParseTreeListener):

    # Enter a parse tree produced by miniJavaExprParser#goal.
    def enterGoal(self, ctx:miniJavaExprParser.GoalContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#goal.
    def exitGoal(self, ctx:miniJavaExprParser.GoalContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#mainclass.
    def enterMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#mainclass.
    def exitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#classdeclaration.
    def enterClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#classdeclaration.
    def exitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#vardeclaration.
    def enterVardeclaration(self, ctx:miniJavaExprParser.VardeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#vardeclaration.
    def exitVardeclaration(self, ctx:miniJavaExprParser.VardeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#methoddeclaration.
    def enterMethoddeclaration(self, ctx:miniJavaExprParser.MethoddeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#methoddeclaration.
    def exitMethoddeclaration(self, ctx:miniJavaExprParser.MethoddeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#arraymjtype.
    def enterArraymjtype(self, ctx:miniJavaExprParser.ArraymjtypeContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#arraymjtype.
    def exitArraymjtype(self, ctx:miniJavaExprParser.ArraymjtypeContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#booleanmjtype.
    def enterBooleanmjtype(self, ctx:miniJavaExprParser.BooleanmjtypeContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#booleanmjtype.
    def exitBooleanmjtype(self, ctx:miniJavaExprParser.BooleanmjtypeContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#intmjtype.
    def enterIntmjtype(self, ctx:miniJavaExprParser.IntmjtypeContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#intmjtype.
    def exitIntmjtype(self, ctx:miniJavaExprParser.IntmjtypeContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#identifiermjtype.
    def enterIdentifiermjtype(self, ctx:miniJavaExprParser.IdentifiermjtypeContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#identifiermjtype.
    def exitIdentifiermjtype(self, ctx:miniJavaExprParser.IdentifiermjtypeContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#blockStatement.
    def enterBlockStatement(self, ctx:miniJavaExprParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#blockStatement.
    def exitBlockStatement(self, ctx:miniJavaExprParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#ifStatement.
    def enterIfStatement(self, ctx:miniJavaExprParser.IfStatementContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#ifStatement.
    def exitIfStatement(self, ctx:miniJavaExprParser.IfStatementContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#whileStatement.
    def enterWhileStatement(self, ctx:miniJavaExprParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#whileStatement.
    def exitWhileStatement(self, ctx:miniJavaExprParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#printStatement.
    def enterPrintStatement(self, ctx:miniJavaExprParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#printStatement.
    def exitPrintStatement(self, ctx:miniJavaExprParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#assignStatement.
    def enterAssignStatement(self, ctx:miniJavaExprParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#assignStatement.
    def exitAssignStatement(self, ctx:miniJavaExprParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#constIntExpr.
    def enterConstIntExpr(self, ctx:miniJavaExprParser.ConstIntExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#constIntExpr.
    def exitConstIntExpr(self, ctx:miniJavaExprParser.ConstIntExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#createClassExpr.
    def enterCreateClassExpr(self, ctx:miniJavaExprParser.CreateClassExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#createClassExpr.
    def exitCreateClassExpr(self, ctx:miniJavaExprParser.CreateClassExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#arraylenExpr.
    def enterArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#arraylenExpr.
    def exitArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#thisExpr.
    def enterThisExpr(self, ctx:miniJavaExprParser.ThisExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#thisExpr.
    def exitThisExpr(self, ctx:miniJavaExprParser.ThisExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#createArrayExpr.
    def enterCreateArrayExpr(self, ctx:miniJavaExprParser.CreateArrayExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#createArrayExpr.
    def exitCreateArrayExpr(self, ctx:miniJavaExprParser.CreateArrayExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#arrayValExpr.
    def enterArrayValExpr(self, ctx:miniJavaExprParser.ArrayValExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#arrayValExpr.
    def exitArrayValExpr(self, ctx:miniJavaExprParser.ArrayValExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#constIdenExpr.
    def enterConstIdenExpr(self, ctx:miniJavaExprParser.ConstIdenExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#constIdenExpr.
    def exitConstIdenExpr(self, ctx:miniJavaExprParser.ConstIdenExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#operationExpr.
    def enterOperationExpr(self, ctx:miniJavaExprParser.OperationExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#operationExpr.
    def exitOperationExpr(self, ctx:miniJavaExprParser.OperationExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#oppExpr.
    def enterOppExpr(self, ctx:miniJavaExprParser.OppExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#oppExpr.
    def exitOppExpr(self, ctx:miniJavaExprParser.OppExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#prioExpr.
    def enterPrioExpr(self, ctx:miniJavaExprParser.PrioExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#prioExpr.
    def exitPrioExpr(self, ctx:miniJavaExprParser.PrioExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#classPropExpr.
    def enterClassPropExpr(self, ctx:miniJavaExprParser.ClassPropExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#classPropExpr.
    def exitClassPropExpr(self, ctx:miniJavaExprParser.ClassPropExprContext):
        pass


    # Enter a parse tree produced by miniJavaExprParser#constBooleanExpr.
    def enterConstBooleanExpr(self, ctx:miniJavaExprParser.ConstBooleanExprContext):
        pass

    # Exit a parse tree produced by miniJavaExprParser#constBooleanExpr.
    def exitConstBooleanExpr(self, ctx:miniJavaExprParser.ConstBooleanExprContext):
        pass


