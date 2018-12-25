import antlr4
from miniJavaExprVisitor import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# A visitor class for detecting semantic errors

mjtype_list = ['int[]', 'boolean', 'int']

class semanticErrorDetection(miniJavaExprVisitor):
    def __init__(self,symbolTable,debug=False):
        super().__init__()
        self.symbolTable = symbolTable
        # identify the action space
        self.classname = ""     # current class
        self.methodname = ""    # current method
        self.debug = debug
    
    def _lookupTable(self, identifier):
        """
        look up identifier in the correspoding symbol table
        return is a dict contains type of identifier
        if identifier is an instance of a user-defined class, dict also contains 'template_class' attr
        if identifier is a method, dict also contains the params list attr 'param_list' and return type 'rtr_type'
        """
        current_method_region = {}
        current_class_region = self.symbolTable.get(self.classname,{})
        if self.methodname != "":
            current_method_region = current_class_region.get(self.methodname,{})
        
        if identifier in current_method_region:
            return current_method_region[identifier]
        elif identifier in current_class_region:
            if current_class_region[identifier]["type"] == "method":
                rtr = {}
                rtr["type"] = current_class_region[identifier]["type"]
                rtr["return_type"] = current_class_region[identifier]["return_type"]
                return rtr
            else:
                return current_class_region[identifier]
        elif identifier in self.symbolTable:
            return {"type":"class", "template_class":identifier}
        else:
            return {"type":"undefined"}

    def _checkAttribute(self, classname, attriname):
        class_region = self.symbolTable.get(classname, {})
        if attriname in class_region:
            return True
        else:
            return False

    def _printErrMsg(self, line, col, msg):
        print("Error(line " + str(line) + " , position " + str(col) + "): " + msg + ".")
    
    def visitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        if self.debug:
            print("visit main class")
        
        node = ctx.IDENTIFIER()[0]
        token = node.getSymbol()
        self.classname = token.text
        self.visitChildren(ctx)

    def visitClassdeclaration(self, ctx:miniJavaExprParser.ClassdeclarationContext):
        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is type([]) and len(identifier_nodes) > 1:
            # has parent class
            cclass_node = identifier_nodes[0]; token = cclass_node.getSymbol(); self.classname = token.text
            pclass_node = identifier_nodes[1]; token = pclass_node.getSymbol()
            pclass_type = self._lookupTable(token)
            line = token.line; col = token.column
            if pclass_type["type"] == "undefined":
                self._printErrMsg(line, col, token.text + " is used without defined")
            elif pclass_type["type"] != "class":
                self._printErrMsg(line, col, "Can't extends type " + pclass_type["type"])
        else:
            if type(identifier_nodes) is type([]) and len(identifier_nodes) == 1:
                cclass_node = identifier_nodes[0]
            else:
                cclass_node = identifier_nodes
            token = cclass_node.getSymbol()
            self.classname = token.text

        if self.debug:
            print("visit class declaration")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        self.visitChildren(ctx)

    def visitMethoddeclaration(self, ctx:miniJavaExprParser.MethoddeclarationContext):
        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is type([]) and len(identifier_nodes) > 1:
            node = identifier_nodes[0]; token = node.getSymbol()
            self.methodname = token.text 
        else:
            if type(identifier_nodes) is type([]):
                node = identifier_nodes[0]
            else:
                node = identifier_nodes
            token = node.getSymbol()
            self.methodname = token.text
        
        # return type check
        rtrexpr = ctx.expression()
        rtrtype = self.visit(rtrexpr)
        methodinfo = self._lookupTable(token.text)
        line = rtrexpr.start.line; col = rtrexpr.start.column
        if methodinfo["return_type"] in mjtype_list and rtrtype["type"] != methodinfo["return_type"]:
            self._printErrMsg(line, col, " return type mismatch, expect type " + methodinfo["return_type"] + " ,but get type " + rtrtype["type"])
        elif methodinfo["return_type"] not in mjtype_list:
            if "template_class" not in rtrtype:
                self._printErrMsg(line, col, " return type mismatch, expect type " + methodinfo["return_type"] + " ,but get type " + rtrtype["type"])
            elif rtrtype["template_class"] != methodinfo["return_type"]:
                self._printErrMsg(line, col, " return type mismatch, expect type " + methodinfo["return_type"] + " ,but get type " + rtrtype["template_class"])


        if self.debug:
            print("visit method declaration")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        self.visitChildren(ctx)

    def visitAssignStatement(self, ctx:miniJavaExprParser.AssignStatementContext):
        if self.debug:
            print("visit assign statement")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        line = token.line; col = token.column

        if idtype["type"] == "undefined":
            self._printErrMsg(line, col, token.text + " is used before defined")

        exprtype = self.visit(ctx.expression())
        if idtype["type"] != exprtype["type"]:
            if idtype["type"] == "instance" and exprtype["type"] == "class":
                if idtype["template_class"] != exprtype["template_class"]:
                    errmsg = "Can't assign object " + exprtype["template_class"] + " to object " + idtype["template_class"]
                    self._printErrMsg(line, col ,errmsg)
            else:
                errmsg = "Can't assign type " + exprtype["type"] + " to type " + idtype["type"]
                self._printErrMsg(line, col, errmsg)
        else:
            if idtype["type"] == "instance":
                if idtype["template_class"] != exprtype["template_class"]:
                    errmsg = "Can't assign object " + exprtype["template_class"] + " to object " + idtype["template_class"]
                    self._printErrMsg(line, col, errmsg)
    
        #if self.debug:
        #print("in assign statement, Identifier type: ", idtype)
        #print("in assign statement, expression type: ", exprtype)

        #self.visitChildren(ctx)

    def visitArrayAssignStatement(self, ctx:miniJavaExprParser.ArrayAssignStatementContext):
        if self.debug:
            print("visit array assign statement")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        identifier_node = ctx.IDENTIFIER()
        token = identifier_node.getSymbol()
        idtype = self._lookupTable(token.text)
        line = token.line; col = token.column
        if idtype["type"] == "undefined":
            errmsg = token.text + " is used without defined"
            self._printErrMsg(line, col, errmsg)
        elif idtype["type"] != "int[]":
            errmsg = idtype["type"] + " object is not iterable"
            self._printErrMsg(line, col, errmsg)
        
        idxexpr = ctx.expression(0)
        idxtype = self.visit(idxexpr)
        line = idxexpr.start.line
        col = idxexpr.start.column
        if idxtype["type"] != "int":
            self._printErrMsg(line, col, "array indices must be integers not " + idxtype["type"])
        
        # currently only int[] array type
        valexpr = ctx.expression(1)
        valtype = self.visit(valexpr)
        line = valexpr.start.line
        col = valexpr.start.column
        if valtype["type"] != "int":
            self._printErrMsg(line, col, "incompatible type, can't assign type int with type " + valtype["type"])
        
        #self.visitChildren(ctx)

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
            self._printErrMsg(line, col, "Incompatible type, type " + exp1type["type"] + " can't calculated with type " + exp2type["type"])
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
        if exp1type["type"] != "int[]":
            line = exp1.start.line; col = exp1.start.column
            self._printErrMsg(line, col, exp1type["type"] + " object is not iterable")
        if exp2type["type"] != "int":
            line = exp2.start.line; col = exp2.start.column
            self._printErrMsg(line, col, "array indices must be integers not " + exp2type["type"])

        return {"expr_type":"arrayVal","type":"int"}

    def visitArraylenExpr(self, ctx:miniJavaExprParser.ArraylenExprContext):
        if self.debug:
            print("visit array len expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        exp = ctx.expression()
        exptype = self.visit(exp)
        line = exp.start.line; col = exp.start.column
        if exptype["type"] != "int[]":
            self._printErrMsg(line, col, exptype["type"] + " object doesn't have attribute length")

        return {"expr_type":"arrayLen","type":"int"}
    
    def _argCheck(self, ctx):
        if self.debug:
            print("visit ClassPropExpr")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        # get method name
        method_name = str(ctx.getChild(2))
        try:
            expr = ctx.expression(0)
        except:
            expr = ctx.expression()
        class_name = self.visit(expr)['template_class']

        line = ctx.start.line
        col = ctx.start.column
        
        # method_arg_list
        arg_type_list = []
        arg_first_flag = 0
        for expr_ctx in ctx.expression():
            if arg_first_flag == 0:
                arg_first_flag = 1
                continue
            
            exp_type = self.visit(expr_ctx)
            arg_type_list.append(exp_type)
        
        arg_right_list = self.symbolTable[class_name][method_name]['arg_list']
        rtr_type = self.symbolTable[class_name][method_name]['return_type']

        # len of arg list
        if len(arg_type_list) != len(arg_right_list):
            print("Error(line " + str(line) + " , position " + str(col) + "): Wrong Argument Numbers.")
        # arg type
        else:
            length = len(arg_right_list)
            for i in range(length):
                arg_type = arg_type_list[i]
                if arg_type['type'] == 'instance':
                    if arg_type['template_class'] != arg_right_list[i]['arg_type']:
                        print("Error(line " + str(line) + " , position " + str(col) + "): Wrong Argument Type.")
                        break
                else:
                    if arg_type['type'] != arg_right_list[i]['arg_type']:
                        print("Error(line " + str(line) + " , position " + str(col) + "): Wrong Argument Type.")
                        break
        return

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
            self._printErrMsg(line, col, exprtype["type"] + " object doesn't have attribute " + cmethodname)
            return {"expr_type": "classProp", "type":"None"}
        elif not self._checkAttribute(exprtype["template_class"], cmethodname):
            self._printErrMsg(line, col, "class " +  exprtype["template_class"] + " doesn't have attribute " + cmethodname)
            return {"expr_type": "classProp", "type":"None"}
        
        # check the paramters
        # temporaly change self.classname to the caller classname
        #print("in classProp, class instance type: ", exprtype)
        
        currentClass = self.classname; currentMethod = self.methodname
        self.classname = exprtype["template_class"]; self.methodname = ""
        methodinfo = self._lookupTable(cmethodname)
        rtrType = methodinfo.get("return_type","undefined")
        self.classname = currentClass; self.methodname = currentMethod

        self._argCheck(ctx)

        if rtrType in mjtype_list:
            return {"expr_type":"classProp", "type":rtrType}
        else:
            return {"expr_type":"classProp", "type":"instance", "template_class":rtrType}
    
    def visitConstIntExpr(self, ctx:miniJavaExprParser.ConstIntExprContext):
        if self.debug:
            print("visit const int")

        return {"expr_type":"constInt", "type":"int"}
    
    def visitConstBooleanExpr(self, ctx:miniJavaExprParser.ConstBooleanExprContext):
        if self.debug:
            print("visit const boolean")

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
            self._printErrMsg(line, col, token.text + " is used without defined")
        for k,v in idtype.items():
            rtr[k] = v
        return rtr
    
    def visitThisExpr(self, ctx:miniJavaExprParser.ThisExprContext):
        if self.debug:
            print("visit this expression")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        return {"expr_type":"this", "type":"class", "template_class":self.classname}
    
    def visitCreateClassExpr(self, ctx:miniJavaExprParser.CreateClassExprContext):
        token = ctx.IDENTIFIER().getSymbol()
        identifier = token.text

        if self.debug:
            print("visit create class expression, new class name ", identifier)
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        line = token.line; col = token.column
        idtype = self._lookupTable(identifier)
        rtr = {"expr_type":"createClass"}
        if idtype["type"] == "undefined":
            self._printErrMsg(line, col, identifier + " is used without defined")
        elif idtype["type"] != "class":
            self._printErrMsg(line, col, "Can't new type " + idtype["type"])
        for k,v in idtype.items():
            rtr[k] = v
        return rtr
    
    def visitCreateArrayExpr(self, ctx:miniJavaExprParser.CreateArrayExprContext):
        expr = ctx.expression()
        exprtype = self.visit(expr)
        line = expr.start.line; col = expr.start.column
        if exprtype["type"] != "int":
            self._printErrMsg(line, col, "type error, expect type int but got type " + exprtype["type"])
        rtr = {"type":"int[]", "expr_type":"createArray"}
        return rtr
    
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