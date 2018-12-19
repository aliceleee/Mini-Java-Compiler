lexer grammar miniJavaLexer;

// Operation Category
IDENTIFIER: [A-Za-z$_][a-zA-Z\d_$]*;
INT: [0-9]+;
WS: [\t\r\n]+ -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? '\n' -> skip;
BOOLEAN: 'true'|'false';
RETURN: 'return';
//RESERVED_KEYWORD: 'abstract'|'assert'|'boolean'|'break'|'byte'|'case'|'catch'|'char'|'class'|'const'|'continue'|'default'|'double'|'do'|'else'|'enum'|'extends'|'final'|'finally'|'float'|'for'|'goto'|'if'|'implements'|'import'|'instanceof'|'int'|'interface'|'long'|'native'|'new'|'null'|'package'|'private'|'protected'|'public'|'return'|'short'|'static'|'strictfp'|'super'|'switch'|'synchronized'|'this'|'throw'|'throws'|'transient'|'true'|'try'|'void'|'volatile'|'while';
