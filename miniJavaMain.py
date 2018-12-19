import sys
from antlr4 import *
from miniJavaExprLexer import *
from miniJavaExprParser import *
from miniJavaExprListener import *

def main(filename):
    filestream = FileStream(filename)
    lexer = miniJavaExprLexer(filestream)
    tokens = CommonTokenStream(lexer)
    parser = miniJavaExprParser(tokens)
    tree = parser.goal()
    print(tree.toStringTree())

if __name__ == "__main__":
    main("./testCode/Factorial.java")