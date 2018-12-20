from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaExprParser import miniJavaExprParser
else:
    from miniJavaExprParser import miniJavaExprParser

# A visitor class for detecting all lex error

reserved_words = ['abstract','assert','boolean','break','byte','case','catch','char','class','const','continue','default','double','do','else','enum','extends','final','finally','float','for','goto','if','implements','import','instanceof','int','interface','long','native','main','new','null','package','private','protected','public','return','short','static','strictfp','super','switch','synchronized','this','throw','throws','transient','try','void','volatile','while']

class LexError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
class lexErrorDetection(ParseTreeVisitor):
    def __init__(self):
        super().__init__()
    
    def checkIdentifier(self, identifier):
        if identifier in reserved_words:
            raise LexError(identifier + " is a reserved word, can't use it as variable name.")

    def visitMainclass(self, ctx:miniJavaExprParser.MainclassContext):
        identifier_nodes = ctx.IDENTIFIER()
        for node in identifier_nodes:
            token = node.getSymbol()
            identifier = token.text
            try: self.checkIdentifier(identifier)
            except Exception as e:
                line = token.line
                col = token.start
                print("Error(line " + str(line) + " , position " + str(col) + "): " + e.msg)
