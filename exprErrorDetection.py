from antlr4 import *
from miniJavaExprVisitor import *

if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser


# A visitor class for detecting all expr error
symbol_table = {}
# customized mjtype list
mjtype_list = ['int[]', 'boolean', 'int']


def visit_var_node(table, ctx):
    var_type = ctx.mjtype().getText()
    var_name = str(ctx.getChild(1))

    table[var_name] = {}
    if var_type in mjtype_list:
        table[var_name]['type'] = var_type
    else:
        table[var_name]['type'] = 'instance'
        table[var_name]['template_class'] = var_type



def visit_method_node(table, ctx):
    # method_name
    method_name = str(ctx.getChild(2))
    # print(method_name)
    table[method_name] = {}
    table[method_name]['type'] = 'method'
    table[method_name]['return_type'] = str(ctx.getChild(1).getText())

    table[method_name]['arg_list'] = []
    child_count = ctx.getChildCount()

    args_flag = 0
    for child_index in range(child_count):
        if str(ctx.getChild(child_index))[0] == '(':
            args_flag = 1
            continue

        if args_flag == 0:
            continue

        # mjtype
        if str(ctx.getChild(child_index))[0] == '[':
            arg_dict = {}
            arg_dict[str(ctx.getChild(child_index + 1))] = ctx.getChild(child_index).getText()
            table[method_name]['arg_list'].append(arg_dict)
        
        if str(ctx.getChild(child_index)) == ')':
            break
    

    for child_ctx in ctx.vardeclaration():
        visit_var_node(table, child_ctx)


class ExprError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class exprErrorDetection(miniJavaExprVisitor):

    def __init__(self):
        super().__init__()
    

    def visitVardeclaration(self, ctx):
        # add to symbol table
        symbol_table[str(ctx.getChild(1))] = ctx.mjtype().getText()


    def visitClassdeclaration(self, ctx):
        class_name = str(ctx.getChild(1))
        symbol_table[class_name] = {
            'type': 'class',
        }

        for child_ctx in ctx.vardeclaration():
            visit_var_node(symbol_table[class_name], child_ctx)
        
        for child_ctx in ctx.methoddeclaration():
            visit_method_node(symbol_table[class_name], child_ctx)

        # print(symbol_table)
        
    
