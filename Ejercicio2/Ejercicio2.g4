grammar Ejercicio2;

s : expr ;

expr
    : term (( '+' | '-' ) term)*
    ;

term
    : factor (( '*' | '/' ) factor)*
    ;

factor
    : 'a'
    | '(' expr ')'
    ;

WS : [ \t\r\n]+ -> skip ;