/* expression analysis rules file */
grammar miniJavaExpr;
/* import lex analysis rules file */
import miniJavaLexer;

goal : mainclass(classdeclaration)*;

mainclass : CLASS IDENTIFIER '{' PUBLIC STATIC VOID MAIN '(' STRING '[' ']' IDENTIFIER ')' '{' statement '}' '}';

classdeclaration : CLASS IDENTIFIER (EXTENDS IDENTIFIER)? '{' (vardeclaration)* (methoddeclaration)* '}';

vardeclaration : mjtype IDENTIFIER ';';

methoddeclaration : PUBLIC mjtype IDENTIFIER '(' (mjtype IDENTIFIER (',' mjtype IDENTIFIER)*)? ')' '{' (vardeclaration)* (statement)* RETURN expression ';' '}';

mjtype : INT '['']'   # arraymjtype
     | BOOLEAN      # booleanmjtype
     | INT          # intmjtype
     | IDENTIFIER   # identifiermjtype
     ;

statement : '{' (statement)* '}'                                    # blockStatement
          | IF '(' expression ')' statement ELSE statement      # ifStatement
          | WHILE '(' expression ')' statement                    # whileStatement
          | PRINT '(' expression ')' ';'             # printStatement
          | IDENTIFIER '=' expression ';'                           # assignStatement
          | IDENTIFIER '[' expression ']' '=' expression ';'        # assignStatement
          ;

expression : expression ('&&' | '<' | '+' | '-' | '*') expression                   # operationExpr
           | expression '[' expression ']'                                          # arrayValExpr
           | expression '.' 'length'                                                # arraylenExpr
           | expression '.' IDENTIFIER '(' (expression (',' expression)*)? ')'      # classPropExpr
           | INTERGER_LITERAL                                                                    # constIntExpr
           | BOOLEAN_LITERAL                                                                # constBooleanExpr
           | IDENTIFIER                                                             # constIdenExpr
           | THIS                                                                 # thisExpr
           | NEW INT '[' expression ']'                                         # createArrayExpr
           | NEW IDENTIFIER '(' ')'                                               # createClassExpr
           | '!' expression                                                         # oppExpr
           | '(' expression ')'                                                     # prioExpr
           ;

rtr : RETURN expression ';';        # return