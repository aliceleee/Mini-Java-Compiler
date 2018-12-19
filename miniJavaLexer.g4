lexer grammar miniJavaLexer;

// Operation Category
INTERGER_LITERAL: [0-9]+;
WS: [ \t\r\n]+ -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? '\n' -> skip;
BOOLEAN_LITERAL: 'true'|'false';
RETURN: 'return';
CLASS: 'class';
IF: 'if';
WHILE: 'while';
ELSE: 'else';
STRING: 'String';
PUBLIC: 'public';
STATIC: 'static';
VOID: 'void';
MAIN: 'main';
EXTENDS: 'extends';
INT:'int';
BOOLEAN: 'boolean';
PRINT: 'System.out.println';
THIS: 'this';
NEW: 'new';
IDENTIFIER: [A-Za-z$_][a-zA-Z0-9_$]*;
//RESERVED_KEYWORD: 'abstract'|'assert'|'boolean'|'break'|'byte'|'case'|'catch'|'char'|'class'|'const'|'continue'|'default'|'double'|'do'|'else'|'enum'|'extends'|'final'|'finally'|'float'|'for'|'goto'|'if'|'implements'|'import'|'instanceof'|'int'|'interface'|'long'|'native'|'new'|'null'|'package'|'private'|'protected'|'public'|'return'|'short'|'static'|'strictfp'|'super'|'switch'|'synchronized'|'this'|'throw'|'throws'|'transient'|'true'|'try'|'void'|'volatile'|'while';