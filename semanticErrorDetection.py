from miniJavaExprVisitor import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# A visitor class for detecting semantic errors

testSymbolTable = {"Factorial":"class", "num_i":"int", "num_arr":"array"}

class semanticException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
class semanticErrorDetection(miniJavaExprVisitor):
    def __init__(self):
        super().__init__()
        self.classname = ""
        self.methodname = ""
    def _lookupTable(self, identifier):
        return testSymbolTable.get(identifier, "undefined")
    def typeCheck(self, identifier, expectedType):
        itype = self._lookupTable(identifier)
        if itype == "undefined": raise semanticException(identifier + " is used without defined.")
        elif itype != expectedType: raise semanticException("Expected type '" + expectedType + "' , while get type '" + itype + "'.")
    def visitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        node = ctx.IDENTIFIER()[0]
        token = node.getSymbol()
        self.classname = token.text
        self.visitChildren(ctx)
    def visitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        identifier_nodes = ctx.IDENTIFIER()
        print(identifier_nodes)
        if type(identifier_nodes) is type([]) and len(identifier_nodes) > 1:
            # has parent class
            cclass_node = identifier_nodes[0]; token = cclass_node.getSymbol(); self.classname = token.text
            pclass_node = identifier_nodes[1]; token = pclass_node.getSymbol()
            try: self.typeCheck(token.text, 'class')
            except Exception as e:
                line = token.line; col = token.column 
                print("Error(line " + str(line) + " , position " + str(col) + "): " + e.msg)
        else:
            if type(identifier_nodes) is type([]) and len(identifier_nodes) == 1:
                cclass_node = identifier_nodes[0]
            else:
                cclass_node = identifier_nodes
            token = cclass_node.getSymbol(); self.classname = token.text
        self.visitChildren(ctx)
    def visitMethoddeclaration(self, ctx:miniJavaExprParser.MethoddeclarationContext):
        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is type([]) and len(identifier_nodes) > 1:
            node = identifier_nodes[0]; token = node.getSymbol()
            self.methodname = token.text 
        else:
            node = identifier_nodes; token = node.getSymbol()
            self.methodname = token.text 
        self.visitChildren(ctx)
    def visitAssignStatement(self, ctx:miniJavaExprParser.AssignStatementContext):
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        line = token.line; col = token.column
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        else:
            exprtype = self.visit(ctx.expression())
            if exprtype != idtype:
                print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, can't assign type " + idtype + " with type " + exprtype + ".")
        self.visitChildren(ctx)
    def visitArrayAssignStatement(self, ctx:miniJavaExprParser.ArrayAssignStatementContext):
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        line = token.line; col = token.column
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        elif idtype != "array":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + idtype + " object is not iterable.")
        
        idxtype = self.visit(ctx.expression(0))
        idxexpr = ctx.expression(0)
        print(idxexpr)
        print(type(idxexpr))
        print(dir(idxexpr))
        line = idxexpr.start.line, col = idxexpr.start.column
        if idxtype != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): array indices must be integers not " + idxtype + ".")
        
        # currently only int[] array type
        valtype = self.visit(ctx.expression(1))
        valexpr = ctx.expression(1)
        line = valexpr.start.line; col = valexpr.start.column
        if valtype != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, can't assign type int with type " + valtype + ".")
        self.visitChildren(ctx)
    def visitOperationExpr(self, ctx:miniJavaExprParser.OperationExprContext):
        exp1 = ctx.expression(0); exp2 = ctx.expression(1)
        exp1type = self.visit(exp1)
        exp2type = self.visit(exp2)
        line = exp1.start.line; col = exp1.start.column
        if exp1type != exp2type:
            print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, type " + exp1type + " can't calculated with type " + exp2type + ".")
        self.visitChildren(ctx)
        return "operation"
    def visitArrayValExpr(self, ctx:miniJavaExprParser.ArrayValExprContext):
        exp1 = ctx.expression(0); exp2 = ctx.expression(1)
        exp1type = self.visit(exp1)
        exp2type = self.visit(exp2)
        if exp1type != "array":
            line = exp1.start.line; col = exp1.start.column
            print("Error(line " + str(line) + " , position " + str(col) + "): " + exp1type + " object is not iterable.")
        if exp2type != "int":
            line = exp2.start.line; col = exp2.start.column
            print("Error(line " + str(line) + " , position " + str(col) + "): array indices must be integers not " + exp2type + ".")
        self.visitChildren(ctx)
        return "int"
    def visitArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        exp = ctx.expression()
        exptype = self.visit(exp)
        line = exp.start.line; col = exp.start.column
        if exptype != "array":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + exptype + " object doesn't have attribute length.")
        self.visitChildren(ctx)
        return "int"
    def visitClassPropExpr(self, ctx:miniJavaExprParser.ClassPropExprContext):
        
        self.visitChildren(ctx)
        return "classProp"
    def visitConstIntExpr(self, ctx:miniJavaExprParser.ConstIntExprContext):
        return "int"
    def visitConstBooleanExpr(self, ctx:miniJavaExprParser.ConstBooleanExprContext):
        return "boolean"
    def visitConstIdenExpr(self, ctx:miniJavaExprParser.ConstIdenExprContext):
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        line = token.line; col = token.column 
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        return idtype