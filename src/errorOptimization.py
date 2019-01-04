from antlr4.error.ErrorListener import *


class miniJavaErrorOptimization(ErrorListener):
    def __init__(self):
        super().__init__()
        self.error_dict = {}
    

    def syntaxError(self, recognizer, offendingSymbol, line, charPositionLine, msg, e):
        #print(dir(recognizer))
        #print(recognizer.getErrorHeader(e))
        #print(recognizer.getExpectedTokens())
        print("Error(line " + str(line) + " , position " + str(charPositionLine) + "): " + msg)
        if 'missing \';\'' in msg:
            if 'semi' not in self.error_dict.keys():
                self.error_dict['semi'] = []
            self.error_dict['semi'].append(line)