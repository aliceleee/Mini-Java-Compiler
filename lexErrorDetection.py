from antlr4 import *
from miniJavaExprVisitor import *

if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser
# A visitor class for detecting all lex error


reserved_words = ['abstract','assert','boolean','break','byte','case','catch','char','class','const','continue','default','double','do','else','enum','extends','final','finally','float','for','goto','if','implements','import','instanceof','int','interface','long','native','main','new','null','package','private','protected','public','return','short','static','strictfp','super','switch','synchronized','this','throw','throws','transient','try','void','volatile','while']


class LexError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class lexErrorDetection(miniJavaExprVisitor):
    def __init__(self):
        super().__init__() 
    def _checkIdentifier(self, identifier):
        if identifier in reserved_words:
            raise LexError(identifier + " is a reserved word, can't use it as variable name.")
    def _checkNode(self, node):
        token = node.getSymbol()
        identifier = token.text
        try: self._checkIdentifier(identifier)
        except Exception as e:
            line = token.line
            col = token.column
            print("Error(line " + str(line) + " , position " + str(col) + "): " + e.msg)
    def checkIdentifier(self, ctx):
        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is type([]):
            for i in range(len(identifier_nodes)):
                node = identifier_nodes[i]
                self._checkNode(node)
        else:
            node = identifier_nodes
            self._checkNode(node)
    def visitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
    def visitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
    def visitVardeclaration(self, ctx:miniJavaExprParser.VardeclarationContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
    def visitMethoddeclaration(self, ctx:miniJavaExprParser.MethoddeclarationContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
    def visitMjtype(self, ctx:miniJavaExprParser.MjtypeContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
    def visitStatement(self, ctx:miniJavaExprParser.StatementContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
    def visitExpression(self, ctx:miniJavaExprParser.ExpressionContext):
        self.checkIdentifier(ctx)
        return self.visitChildren(ctx)
