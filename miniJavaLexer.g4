lexer grammar miniJavaLexer;

// Operation Category
WS: [ \t\r\n]+ -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? '\n' -> skip;
RESERVED_KEYWORD: 'abstract'|'assert'|'boolean'|'break'|'byte'|'case'|'catch'|'char'|'class'|'const'|'continue'|'default'|'double'|'do'|'else'|'enum'|'extends'|'final'|'finally'|'float'|'for'|'goto'|'if'|'implements'|'import'|'instanceof'|'int'|'interface'|'long'|'native'|'main'|'new'|'null'|'package'|'private'|'protected'|'public'|'return'|'short'|'static'|'strictfp'|'super'|'switch'|'synchronized'|'this'|'throw'|'throws'|'transient'|'try'|'void'|'volatile'|'while';
IDENTIFIER: [A-Za-z$_][a-zA-Z0-9_$]*;
INT: [0-9]+;
BOOLEAN: 'true'|'false';
