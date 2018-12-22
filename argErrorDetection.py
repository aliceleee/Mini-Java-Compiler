from antlr4 import *
from miniJavaExprVisitor import *
from test import *

if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser


class argError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class argErrorDetection(semanticErrorDetection):

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.classname = ""
        self.methodname = ""
        self.debug = False
        super().__init__()
    

    def visitMainclass(self, ctx):
        if self.debug:
            print("visit Mainclass")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)

        node = ctx.IDENTIFIER()[0]
        token = node.getSymbol()
        self.classname = str(node)
        self.visitChildren(ctx)
    
    
    def visitMethoddeclaration(self, ctx):
        if self.debug:
            print("visit Methoddeclaration")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        
        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is type([]) and len(identifier_nodes) > 1:
            node = identifier_nodes[0]
            self.methodname = str(node)
        else:
            node = identifier_nodes
            self.methodname = str(node)
        self.visitChildren(ctx)
    

    def visitClassPropExpr(self, ctx):
        if self.debug:
            print("visit ClassPropExpr")
            print("\tcurrent class: ", self.classname)
            print("\tcurrent method: ", self.methodname)
        # get method name
        method_name = str(ctx.getChild(2))
        class_name = self.visit(ctx)['template_class']

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
        
        arg_right_list = self.symbol_table[class_name][method_name]['arg_list']

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
                else:
                    if arg_type['type'] != arg_right_list[i]['arg_type']:
                        print("Error(line " + str(line) + " , position " + str(col) + "): Wrong Argument Type.")


        
