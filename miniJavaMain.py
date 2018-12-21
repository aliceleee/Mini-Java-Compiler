import sys
from antlr4 import *
from miniJavaExprLexer import *
from miniJavaExprParser import *
from miniJavaExprListener import *
from errorOptimization import *
from lexErrorDetection import *
from symbolTable import *

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
    symbolTable = symbolTable()
    symbolTable.visit(tree)

    lexErrorDetector = lexErrorDetection()
    lexErrorDetector.visit(tree)

    argErrorDetection = argErrorDetection()
    argErrorDetection.visit(tree)




if __name__ == "__main__":
    # main("./testCode/Factorial.java")
    main("./testCases/BinaryTree.java")