/* expression analysis rules file */
grammar miniJavaExpr;
/* import lex analysis rules file */
import miniJavaLexer;

goal : mainclass(classdeclaration)*;

mainclass : 'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}' '}';

classdeclaration : 'class' IDENTIFIER ('extends' IDENTIFIER)? '{' (vardeclaration)* (methoddeclaration)* '}';

vardeclaration : type IDENTIFIER ';';

methoddeclaration : 'public' type IDENTIFIER '(' (type IDENTIFIER (',' type IDENTIFIER)*)? ')' '{' (vardeclaration)* (statement)* 'return' expression ';' '}';

type : 'int' '['']'   # arrayType
     | 'boolean'      # booleanType
     | 'int'          # intType
     | IDENTIFIER   # identifierType
     ;

statement : '{' (statement)* '}'
          | 'if' '(' expression ')' statement 'else' statement      # ifStatement
          | 'while' '(' expression ')' statement                    # whileStatement
          | 'System.out.println' '(' expression ')' ';'             # printStatement
          | IDENTIFIER '=' expression ';'                           # assignStatement
          | IDENTIFIER '[' expression ']' '=' expression ';'        # assignStatement
          ;

expression : expression ('&&' | '<' | '+' | '-' | '*') expression                   # operationExpr
           | expression '[' expression ']'                                          # arrayValExpr
           | expression '.' 'length'                                                # arraylenExpr
           | expression '.' IDENTIFIER '(' (expression (',' expression)*)? ')'      # classPropExpr
           | INT                                                                    # constIntExpr
           | BOOLEAN
           | IDENTIFIER
           | 'this'
           | 'new' 'int' '[' expression ']'                                         # createArrayExpr
           | 'new' IDENTIFIER '(' ')'                                               # createClassExpr
           | '!' expression
           | '(' expression ')'
           ;

