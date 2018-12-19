/* expression analysis rules file */
grammar miniJavaExpr;
/* import lex analysis rules file */
import miniJavaLexer;

goal : mainclass(classdeclaration)*;

mainclass : class IDENTIFIER '{' public static void main '(' string '[' ']' IDENTIFIER ')' '{' statement '}' '}';

classdeclaration : class IDENTIFIER (extends IDENTIFIER)? '{' (vardeclaration)* (methoddeclaration)* '}';

vardeclaration : mjtype IDENTIFIER ';';

methoddeclaration : PUBLIC mjtype IDENTIFIER '(' (mjtype IDENTIFIER (',' mjtype IDENTIFIER)*)? ')' '{' (vardeclaration)* (statement)* RETURN expression ';' '}';

mjtype : int '['']'   # arraymjtype
     | boolean      # booleanmjtype
     | int          # intmjtype
     | IDENTIFIER   # identifiermjtype
     ;

statement : '{' (statement)* '}'                                    # blockStatement
          | if '(' expression ')' statement else statement      # ifStatement
          | while '(' expression ')' statement                    # whileStatement
          | print '(' expression ')' ';'             # printStatement
          | IDENTIFIER '=' expression ';'                           # assignStatement
          | IDENTIFIER '[' expression ']' '=' expression ';'        # assignStatement
          ;

expression : expression ('&&' | '<' | '+' | '-' | '*') expression                   # operationExpr
           | expression '[' expression ']'                                          # arrayValExpr
           | expression '.' 'length'                                                # arraylenExpr
           | expression '.' IDENTIFIER '(' (expression (',' expression)*)? ')'      # classPropExpr
           | INT                                                                    # constIntExpr
           | BOOLEAN                                                                # constBooleanExpr
           | IDENTIFIER                                                             # constIdenExpr
           | this                                                                 # thisExpr
           | new int '[' expression ']'                                         # createArrayExpr
           | new IDENTIFIER '(' ')'                                               # createClassExpr
           | '!' expression                                                         # oppExpr
           | '(' expression ')'                                                     # prioExpr
           ;

rtr : return expression ';';        # return