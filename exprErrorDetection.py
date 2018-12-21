from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser


# A visitor class for detecting all expr error
symbol_table = dict


class ExprError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class exprErrorDetection(ParseTreeVisitor):

    def __init__(self):
        super().__init__()

    def visitVardeclaration(self, ctx:miniJavaExprParser.MainclassContext):
        
    

