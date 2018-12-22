import sys
from antlr4 import *
from miniJavaExprLexer import *
from miniJavaExprParser import *
from miniJavaExprListener import *
from errorOptimization import *
from lexErrorDetection import *
from symbolTable import *
from argErrorDetection import *
from semanticErrorDetection import *

def main(filename):
    filestream = FileStream(filename)
    lexer = miniJavaExprLexer(filestream)
    tokens = CommonTokenStream(lexer)
    parser = miniJavaExprParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(miniJavaErrorOptimization())
    tree = parser.goal()
    # print(tree.toStringTree())

    # build symbol table
    symbol_table_handler = symbolTable()
    symbol_table_handler.visit(tree)
    symbol_table = symbol_table_handler.symbol_table
    print(symbol_table)

    lexErrorDetector = lexErrorDetection()
    lexErrorDetector.visit(tree)
    semanticErrorDetector = semanticErrorDetection(symbol_table)
    semanticErrorDetector.visit(tree)

    #argErrorDetector = argErrorDetection(symbol_table)
    #argErrorDetector.visit(tree)


if __name__ == "__main__":
    main("./testCode/Factorial.java")
    #main("./testCases/BinaryTree.java")