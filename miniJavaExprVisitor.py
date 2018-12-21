# Generated from miniJavaExpr.g4 by ANTLR 4.7.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by miniJavaExprParser.

class miniJavaExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniJavaExprParser#goal.
    def visitGoal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#mainclass.
    def visitMainclass(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#classdeclaration.
    def visitClassdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#vardeclaration.
    def visitVardeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#methoddeclaration.
    def visitMethoddeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arraymjtype.
    def visitArraymjtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#booleanmjtype.
    def visitBooleanmjtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#intmjtype.
    def visitIntmjtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#identifiermjtype.
    def visitIdentifiermjtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#blockStatement.
    def visitBlockStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#ifStatement.
    def visitIfStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#whileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#printStatement.
    def visitPrintStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#assignStatement.
    def visitAssignStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arrayAssignStatement.
    def visitArrayAssignStatement(self, ctx:miniJavaExprParser.ArrayAssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#constIntExpr.
    def visitConstIntExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#createClassExpr.
    def visitCreateClassExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arraylenExpr.
    def visitArraylenExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#thisExpr.
    def visitThisExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#createArrayExpr.
    def visitCreateArrayExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#arrayValExpr.
    def visitArrayValExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#constIdenExpr.
    def visitConstIdenExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#operationExpr.
    def visitOperationExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#oppExpr.
    def visitOppExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#prioExpr.
    def visitPrioExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#classPropExpr.
    def visitClassPropExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaExprParser#constBooleanExpr.
    def visitConstBooleanExpr(self, ctx):
        return self.visitChildren(ctx)


