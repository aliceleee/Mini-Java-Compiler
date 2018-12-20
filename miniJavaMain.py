import sys
from antlr4 import *
from miniJavaExprLexer import *
from miniJavaExprParser import *
from miniJavaExprListener import *
from errorOptimization import *

def main(filename):
    filestream = FileStream(filename)
    lexer = miniJavaExprLexer(filestream)
    tokens = CommonTokenStream(lexer)
    parser = miniJavaExprParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(miniJavaLexErrorHandler())
    tree = parser.goal()
    print(tree.toStringTree())

if __name__ == "__main__":
    main("./testCode/Factorial.java")