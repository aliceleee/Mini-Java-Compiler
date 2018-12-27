from antlr4 import *
from miniJavaExprVisitor import *
import copy

if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser


# customized mjtype list
mjtype_list = ['int[]', 'boolean', 'int']


def visit_var_node(all_table, table, ctx):
    # print(table)
    var_type = ctx.mjtype().getText()
    var_name = str(ctx.getChild(1))

    if var_type not in mjtype_list:
        table[var_name]['parent_class'] = all_table[var_type]['parent_class']


def visit_method_node(all_table, table, ctx):
    # method_name
    method_name = str(ctx.getChild(2))
    
    for child_ctx in ctx.vardeclaration():
        visit_var_node(all_table, table[method_name], child_ctx)


class symbolTableRound2(miniJavaExprVisitor):

    def __init__(self, symbol_table):
        super().__init__()
        self.symbol_table = symbol_table

    def visitClassdeclaration(self, ctx):
        class_name = str(ctx.getChild(1))

        for child_ctx in ctx.vardeclaration():
            visit_var_node(self.symbol_table, self.symbol_table[class_name], child_ctx)
        
        for child_ctx in ctx.methoddeclaration():
            visit_method_node(self.symbol_table, self.symbol_table[class_name], child_ctx)

        # identifier_nodes = ctx.IDENTIFIER()
        # if type(identifier_nodes) is list and len(identifier_nodes) > 1:
        #     # has parents
        #     pclass = identifier_nodes[1].getSymbol()
        #     if pclass in symbol_table:
        #         pclass_attr = symbol_table[pclass]
        #         for k,v in pclass_attr.items():
        #             if k in symbol_table[class_name]:
        #                 pass
        #             else:
        #                 symbol_table[class_name][k] = v
        # print(symbol_table)