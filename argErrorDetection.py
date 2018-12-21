from antlr4 import *
from miniJavaExprVisitor import *
from symbolTable import symbol_table

if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser


class argErrorDetection(miniJavaExprVisitor):
    def visitClassdeclaration(self, ctx):
        