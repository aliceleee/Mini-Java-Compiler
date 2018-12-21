from miniJavaExprVisitor import *

# A visitor class for detecting semantic errors

testSymbolTable = {"A":"int"}

class semanticException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
class semanticErrorDetection(miniJavaExprVisitor):
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
        line = token.line; col = token.start
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        else:
            exprtype = self.visit(ctx.expression(0))
            if exprtype != idtype:
                print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, can't assign type " + idtype + " with type " + exprtype + ".")
    def visitArrayAssignStatement(self, ctx:miniJavaExprParser.ArrayAssignStatementContext):
        identifier_node = ctx.IDENTIFIER()[0]
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        line = token.line; col = token.start
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        else if idtype != "array":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + idtype + " object is not iterable.")
        
        idxtype = self.visit(ctx.expression(0))
        idxtoken = ctx.expression(0).getSymbol()
        line = idxtoken.line, col = idxtoken.start
        if idxtype != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): array indices must be integers not " + idxtype + ".")
        
        # currently only int[] array type
        valtype = self.visit(ctx.expression(1))
        valtoken = ctx.expression(1).getSymbol()
        line = valtoken.line; col = valtoken.start
        if valtype != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, can't assign type int with type " + valtype + ".")
    def visitOperationExpr(self, ctx:miniJavaExprParser.OperationExprContext):
        pass
    def visitArrayValExpr(self, ctx:miniJavaExprParser.ArrayValExprContext):
        pass
    def visitArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        pass
    def visitClassPropExpr(self, ctx:miniJavaExprParser.ClassPropExprContext):
        pass
    