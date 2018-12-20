from antlr4.error.ErrorListener import *

class miniJavaLexErrorHandler(ErrorListener):
    def __init__(self):
        super().__init__()
    def syntaxError(self, recognizer, offendingSymbol, line, charPositionLine, msg, e):
        #print(dir(recognizer))
        #print(recognizer.getErrorHeader(e))
        #print(recognizer.getExpectedTokens())
        print("Error(line " + str(line) + " , position " + str(charPositionLine) + "): " + msg)