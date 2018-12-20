# Generated from miniJavaExpr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# This class defines a complete generic visitor for a parse tree produced by miniJavaExprParser.

class miniJavaExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniJavaExprParser#goal.
    def visitGoal(self, ctx:miniJavaExprParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#mainclass.
    def visitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#classdeclaration.
    def visitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#vardeclaration.
    def visitVardeclaration(self, ctx:miniJavaExprParser.VardeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#methoddeclaration.
    def visitMethoddeclaration(self, ctx:miniJavaExprParser.MethoddeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arraymjtype.
    def visitArraymjtype(self, ctx:miniJavaExprParser.ArraymjtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#booleanmjtype.
    def visitBooleanmjtype(self, ctx:miniJavaExprParser.BooleanmjtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#intmjtype.
    def visitIntmjtype(self, ctx:miniJavaExprParser.IntmjtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#identifiermjtype.
    def visitIdentifiermjtype(self, ctx:miniJavaExprParser.IdentifiermjtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#blockStatement.
    def visitBlockStatement(self, ctx:miniJavaExprParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#ifStatement.
    def visitIfStatement(self, ctx:miniJavaExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#whileStatement.
    def visitWhileStatement(self, ctx:miniJavaExprParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#printStatement.
    def visitPrintStatement(self, ctx:miniJavaExprParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#assignStatement.
    def visitAssignStatement(self, ctx:miniJavaExprParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#constIntExpr.
    def visitConstIntExpr(self, ctx:miniJavaExprParser.ConstIntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#createClassExpr.
    def visitCreateClassExpr(self, ctx:miniJavaExprParser.CreateClassExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arraylenExpr.
    def visitArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#thisExpr.
    def visitThisExpr(self, ctx:miniJavaExprParser.ThisExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#createArrayExpr.
    def visitCreateArrayExpr(self, ctx:miniJavaExprParser.CreateArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arrayValExpr.
    def visitArrayValExpr(self, ctx:miniJavaExprParser.ArrayValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#constIdenExpr.
    def visitConstIdenExpr(self, ctx:miniJavaExprParser.ConstIdenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#operationExpr.
    def visitOperationExpr(self, ctx:miniJavaExprParser.OperationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#oppExpr.
    def visitOppExpr(self, ctx:miniJavaExprParser.OppExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#prioExpr.
    def visitPrioExpr(self, ctx:miniJavaExprParser.PrioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#classPropExpr.
    def visitClassPropExpr(self, ctx:miniJavaExprParser.ClassPropExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#constBooleanExpr.
    def visitConstBooleanExpr(self, ctx:miniJavaExprParser.ConstBooleanExprContext):
        return self.visitChildren(ctx)



del miniJavaExprParser