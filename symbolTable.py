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
    # print(table)
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
        
        if str(ctx.getChild(child_index)) == ')':
            break

        # mjtype
        if str(ctx.getChild(child_index))[0] == '[':
            arg_dict = {}
            # print(str(ctx.getChild(child_index + 1)))
            arg_dict['arg_name'] = str(ctx.getChild(child_index + 1))
            arg_dict['arg_type'] = ctx.getChild(child_index).getText()
            table[method_name]['arg_list'].append(arg_dict)
    # see all params as defined var
    for d in table[method_name]["arg_list"]:
        if d["arg_type"] in mjtype_list:
            table[method_name][d['arg_name']] = {"type":d["arg_type"]}
        else:
            table[method_name][d['arg_name']] = {"type":"instance", "template_class":d["arg_type"]}
        
    for child_ctx in ctx.vardeclaration():
        visit_var_node(table[method_name], child_ctx)


class symbolTable(miniJavaExprVisitor):

    def __init__(self):
        super().__init__()
        self.symbol_table = symbol_table

    
    def visitMainclass(self, ctx):
        class_name = str(ctx.getChild(1))
        symbol_table[class_name] = {
            'type': 'class',
            'main': {'type': 'method',
                    'return_type': 'void',
                    'arg_list': [{'arg_name':'a', 'arg_type':'String[]'}]
            }
        }

    def visitClassdeclaration(self, ctx):
        class_name = str(ctx.getChild(1))
        symbol_table[class_name] = {
            'type': 'class',
        }

        for child_ctx in ctx.vardeclaration():
            visit_var_node(symbol_table[class_name], child_ctx)
        
        for child_ctx in ctx.methoddeclaration():
            visit_method_node(symbol_table[class_name], child_ctx)

        identifier_nodes = ctx.IDENTIFIER()
        if type(identifier_nodes) is list and len(identifier_nodes) > 1:
            # has parents
            pclass = identifier_nodes[1].getSymbol()
            if pclass in symbol_table:
                pclass_attr = symbol_table[pclass]
                for k,v in pclass_attr.items():
                    if k in symbol_table[class_name]:
                        pass
                    else:
                        symbol_table[class_name][k] = v
        # print(symbol_table)
    
    
