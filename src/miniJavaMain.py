import sys
from antlr4 import *
from miniJavaExprLexer import *
from miniJavaExprParser import *
from miniJavaExprListener import *
from errorOptimization import *
from lexErrorDetection import *
from symbolTable import *
from symbolTableRound2 import *
from argErrorDetection import *
#from semanticErrorDetection import *
from semanticErrorDetection_re import *
from errorFix import *
import argparse
import os

_parser = argparse.ArgumentParser("miniJava Compiler")
_parser.add_argument("--dir", type=str, default="./testCode")
_parser.add_argument("--file", type=str, default="TreeVisitor.java")
args = _parser.parse_args()

def get_tree(filename):
    filestream = FileStream(filename)
    lexer = miniJavaExprLexer(filestream)
    tokens = CommonTokenStream(lexer)
    parser = miniJavaExprParser(tokens)
    parser.removeErrorListeners()
    errorOptimizationInstance = miniJavaErrorOptimization()
    parser.addErrorListener(errorOptimizationInstance)
    tree = parser.goal()
     
    error_dict = errorOptimizationInstance.error_dict
    error_fixer(error_dict, filename)
   
    if error_dict:
        tree = get_tree(filename)
        return tree
    return tree

def main(filename):
    tree = get_tree(filename)
    # print(tree.toStringTree())
    
    # build symbol table
    symbol_table_handler = symbolTable()
    symbol_table_handler.visit(tree)
    symbol_table_round1 = symbol_table_handler.symbol_table
    symbol_table_handler2 = symbolTableRound2(symbol_table_round1)
    symbol_table_handler2.visit(tree)
    symbol_table = symbol_table_handler2.symbol_table

    # print(symbol_table_round1['MyVisitor'])

    lexErrorDetector = lexErrorDetection()
    lexErrorDetector.visit(tree)
    semanticErrorDetector = semanticErrorDetection(symbol_table)
    semanticErrorDetector.visit(tree)
    # print("semantic finish")

    # argErrorDetector = argErrorDetection(symbol_table)
    # argErrorDetector.visit(tree)
    # print ("arg finish")

if __name__ == "__main__":
    dirname = args.dir 
    filename = args.file
    path = os.path.join(dirname, filename)
    main(path)
    # main("./testCode/BinarySearch.java")
    # main("./testCases/Factorial.java")
