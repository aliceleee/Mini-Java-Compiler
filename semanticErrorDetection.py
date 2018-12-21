import antlr4
from miniJavaExprVisitor import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# A visitor class for detecting semantic errors

testSymbolTable = {"Factorial":"class", "Fac":"class", "num":"int", "num_aux": "int", "ComputeFac":"method"}

class semanticException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
class semanticErrorDetection(miniJavaExprVisitor):
    def __init__(self):
        super().__init__()
        # identify the action space
        self.classname = ""     # current class
        self.methodname = ""    # current method
        self.debug = False
    def _lookupTable(self, identifier):
        """
        look up identifier in the correspoding symbol table
        return is a dict contains type of identifier
        if identifier is an instance of a user-defined class, dict also contains 'template_class' attr
        if identifier is a method, dict also contains the params list attr 'param_list' and return type 'rtr_type'
        """
        rtr = {}
        rtr["type"] = testSymbolTable.get(identifier, "undefined")
        return rtr
    
    def _checkAttribute(self, templateClass, methodName):
        #print("caller class: ", templateClass)
        #print("callee method: ", methodName)
        return True
    
    def typeCheck(self, identifier, expectedType):
        itype = self._lookupTable(identifier)["type"]
        if itype == "undefined": raise semanticException(identifier + " is used without defined.")
        elif itype != expectedType: raise semanticException("Expected type '" + expectedType + "' , while get type '" + itype + "'.")
    
    def visitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        if self.debug:
            print("visit main class")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        node = ctx.IDENTIFIER()[0]
        token = node.getSymbol()
        self.classname = token.text
        self.visitChildren(ctx)
    
    def visitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        if self.debug:
            print("visit class declaration")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        identifier_nodes = ctx.IDENTIFIER()
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
        if self.debug:
            print("visit method declaration")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is type([]) and len(identifier_nodes) > 1:
            node = identifier_nodes[0]; token = node.getSymbol()
            self.methodname = token.text 
        else:
            node = identifier_nodes; token = node.getSymbol()
            self.methodname = token.text 
        self.visitChildren(ctx)
    
    def visitAssignStatement(self, ctx:miniJavaExprParser.AssignStatementContext):
        if self.debug:
            print("visit assign statement")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)["type"]
        line = token.line; col = token.column
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        else:
            exprtype = self.visit(ctx.expression())
            if exprtype["type"] != idtype:
                print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, can't assign type " + idtype + " with type " + exprtype["type"] + ".")
        self.visitChildren(ctx)
    
    def visitArrayAssignStatement(self, ctx:miniJavaExprParser.ArrayAssignStatementContext):
        if self.debug:
            print("visit array assign statement")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)["type"]
        line = token.line; col = token.column
        if idtype == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
        elif idtype != "array":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + idtype + " object is not iterable.")
        
        idxtype = self.visit(ctx.expression(0))
        idxexpr = ctx.expression(0)
        line = idxexpr.start.line, col = idxexpr.start.column
        if idxtype["type"] != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): array indices must be integers not " + idxtype["type"] + ".")
        
        # currently only int[] array type
        valtype = self.visit(ctx.expression(1))
        valexpr = ctx.expression(1)
        line = valexpr.start.line; col = valexpr.start.column
        if valtype["type"] != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, can't assign type int with type " + valtype["type"] + ".")
        self.visitChildren(ctx)
    
    def visitOperationExpr(self, ctx:miniJavaExprParser.OperationExprContext):
        if self.debug:
            print("visit operation expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        exp1 = ctx.expression(0); exp2 = ctx.expression(1)
        exp1type = self.visit(exp1)
        exp2type = self.visit(exp2)
        line = exp1.start.line; col = exp1.start.column
        if exp1type["type"] != exp2type["type"]:
            print("Error(line " + str(line) + " , position " + str(col) + "): Incompatible type, type " + exp1type["type"] + " can't calculated with type " + exp2type["type"] + ".")
            return {"expr_type":"operation", "type":"undefined"}
        return {"expr_type":"operation", "type":exp1type["type"]}
    
    def visitArrayValExpr(self, ctx:miniJavaExprParser.ArrayValExprContext):
        if self.debug:
            print("visit array val expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        exp1 = ctx.expression(0); exp2 = ctx.expression(1)
        exp1type = self.visit(exp1)
        exp2type = self.visit(exp2)
        if exp1type["type"] != "array":
            line = exp1.start.line; col = exp1.start.column
            print("Error(line " + str(line) + " , position " + str(col) + "): " + exp1type["type"] + " object is not iterable.")
        if exp2type["type"] != "int":
            line = exp2.start.line; col = exp2.start.column
            print("Error(line " + str(line) + " , position " + str(col) + "): array indices must be integers not " + exp2type["type"] + ".")
        return {"expr_type":"arrayVal","type":"int"}

    def visitArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        if self.debug:
            print("visit array len expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        exp = ctx.expression()
        exptype = self.visit(exp)
        line = exp.start.line; col = exp.start.column
        if exptype["type"] != "array":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + exptype["type"] + " object doesn't have attribute length.")
        return {"expr_type":"arrayLen","type":"int"}
    
    def visitClassPropExpr(self, ctx:miniJavaExprParser.ClassPropExprContext):
        if self.debug:
            print("visit class property expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        # callee method name
        cmethodname = ctx.IDENTIFIER().getSymbol().text
        # whether the caller is a class instance and whether this class has this callee method
        try: expr = ctx.expression(0)
        except: expr = ctx.expression()
        line = expr.start.line; col = expr.start.column
        exprtype = self.visit(expr)
        if exprtype["type"] != "class" and exprtype["type"] != "instance":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + exprtype["type"] + " object doesn't have attribute " + cmethodname + ".")
        elif not self._checkAttribute(exprtype["template_class"], cmethodname):
            print("Error(line " + str(line) + " , position " + str(col) + "): class " + exptype["template_class"] + " doesn't have attribute " + cmethodname + ".")
        # check the paramters
        rtrType = "int" # return type of the callee method
        ###
        return {"expr_type":"classProp", "type":rtrType}
    
    def visitConstIntExpr(self, ctx:miniJavaExprParser.ConstIntExprContext):
        if self.debug:
            print("visit const int")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        return {"expr_type":"constInt", "type":"int"}
    def visitConstBooleanExpr(self, ctx:miniJavaExprParser.ConstBooleanExprContext):
        if self.debug:
            print("visit const boolean")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        return {"expr_type":"constBoolean", "type":"boolean"}
    
    def visitConstIdenExpr(self, ctx:miniJavaExprParser.ConstIdenExprContext):
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()

        if self.debug:
            print("visit const identifier expression ", token.text)
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        idtype = self._lookupTable(token.text)
        line = token.line; col = token.column 
        rtr = {"expr_type":"constIden"}
        if idtype["type"] == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + token.text + " is used without defined.")
            rtr["type"] = "undefined"
        elif idtype["type"] == "instance":
            rtr["type"] = "instance"
            rtr["template_class"] = idtype["template_class"]
        else:
            rtr["type"] = idtype["type"]
        return rtr
    
    def visitThisExpr(self, ctx:miniJavaExprParser.ThisExprContext):
        if self.debug:
            print("visit this expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        return {"expr_type":"this", "type":"class", "template_class":self.classname}
    
    def visitCreateClassExpr(self, ctx:miniJavaExprParser.CreateClassExprContext):
        if self.debug:
            print("visit create class expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        token = ctx.IDENTIFIER().getSymbol()
        identifier = token.text
        line = token.line; col = token.column
        idtype = self._lookupTable(identifier)
        rtr = {"expr_type":"createClass"}
        if idtype["type"] == "undefined":
            print("Error(line " + str(line) + " , position " + str(col) + "): " + identifier + " is used without defined.")
            rtr["type"] = "undefined"
        elif idtype["type"] != "class":
            print("Error(line " + str(line) + " , position " + str(col) + "): Can't new type " + idtype["type"] + ".")
            rtr["type"] = idtype["type"]
        else:
            rtr["type"] = "class"
            rtr["template_class"] = identifier
        return rtr

    def visitCreateArrayExpr(self, ctx:miniJavaExprParser.CreateArrayExprContext):
        expr = ctx.expression()
        exprtype = self.visit(expr)
        line = expr.start.line; col = expr.start.column
        if exprtype["type"] != "int":
            print("Error(line " + str(line) + " , position " + str(col) + "): Type error, expect type int but got type " + exprtype["type"] + ".")

    def visitPrioExpr(self, ctx:miniJavaExprParser.PrintStatementContext):
        if self.debug:
            print("visit prio expr")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        rtr = self.visit(ctx.expression())
        rtr["expr_type"] = "prio"
        return rtr
    
    def visitOppExpr(self, ctx:miniJavaExprParser.OppExprContext):
        if self.debug:
            print("visit opp expr")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        rtr = self.visit(ctx.expression())
        rtr["expr_type"] = "opp"
        return rtr