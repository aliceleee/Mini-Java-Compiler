from antlr4 import *
from miniJavaExprVisitor import *

if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser



class test(miniJavaExprVisitor):
    def __init__(self):
        super().__init__()
    
    def testFunc(self):
        print('test')
    