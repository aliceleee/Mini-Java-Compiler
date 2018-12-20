from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# A visitor class for detecting semantic errors

testSymbolTable = {"A":"int"}

class semanticException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
class semanticErrorDetection(ParseTreeVisitor):
    def __init__(self):
        super().__init__()
    def _lookupTable(self, identifier):
        return testSymbolTable.get(identifier, "undefined")
    def typeCheck(self, identifier, expectedType):
        itype = self._lookupTable(identifier)
        if itype == "undefined": raise semanticException(identifier + " is used without defined.")
        elif itype != expectedType: raise semanticException("Expected type '" + expectedType + "' , while get type '" + itype + "'.")
    def visitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        identifier_nodes = ctx.IDENTIFIER()
        if len(identifier_nodes) > 1:
            # has parent class
            pclass_node = identifier_nodes[1]; token = pclass_node.getSymbol()
            try: self.typeCheck(token.text, 'class')
            except Exception as e:
                line = token.line; col = token.start 
                print("Error(line " + str(line) + " , position " + str(col) + "): " + e.msg)
    def visitAssignStatement(self, ctx.miniJavaExprParser.AssignStatementContext):
        identifier_node = ctx.IDENTIFIER()[0]
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        if idtype == "undefined":
            line = token.line; col = token.start
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        else:
            pass