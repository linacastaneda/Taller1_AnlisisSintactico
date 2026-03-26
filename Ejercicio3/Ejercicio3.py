# EJERCICIO 3 — PRECEDENCIA Y ASOCIATIVIDAD

# Gramática base:
# E → E op E | (E) | num
# op → + | - | * | /

class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __repr__(self):
        if self.izq is None and self.der is None:
            return str(self.valor)
        return f"({self.izq} {self.valor} {self.der})"


def lexer(cadena):
    tokens = []
    i = 0
    while i < len(cadena):
        c = cadena[i]
        if c.isspace():
            i += 1
        elif c.isdigit():
            j = i
            while j < len(cadena) and cadena[j].isdigit():
                j += 1
            tokens.append(cadena[i:j])
            i = j
        else:
            tokens.append(c)
            i += 1
    tokens.append("$")
    return tokens


class ParserPratt:
    def __init__(self, tokens, prec):
        self.tokens = tokens
        self.pos = 0
        self.prec = prec

    def peek(self):
        return self.tokens[self.pos]

    def consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def get_prec(self, op):
        return self.prec.get(op, (0, 'L'))

    def parse_expr(self, min_prec=0):
        lhs = self.parse_primary()

        while True:
            op = self.peek()
            nivel, asoc = self.get_prec(op)

            if nivel == 0 or nivel < min_prec:
                break

            if asoc == 'L' and nivel == min_prec:
                break

            self.consume()

            siguiente = nivel if asoc == 'R' else nivel + 1
            rhs = self.parse_expr(siguiente)

            lhs = Nodo(op, lhs, rhs)

        return lhs

    def parse_primary(self):
        tok = self.peek()

        if tok == "(":
            self.consume()
            nodo = self.parse_expr(0)
            self.consume()
            return nodo

        if tok.isdigit():
            return Nodo(int(self.consume()))

        raise SyntaxError("Error sintáctico")


def evaluar(n):
    if n.izq is None:
        return n.valor

    a = evaluar(n.izq)
    b = evaluar(n.der)

    if n.valor == "+": return a + b
    if n.valor == "-": return a - b
    if n.valor == "*": return a * b
    if n.valor == "/": return a / b


def imprimir(n, pref="", ult=True):
    print(pref + ("└── " if ult else "├── ") + str(n.valor))
    hijos = [h for h in (n.izq, n.der) if h]
    for i, h in enumerate(hijos):
        imprimir(h, pref + ("    " if ult else "│   "), i == len(hijos)-1)


if __name__ == "__main__":

    print("GRAMÁTICA:")
    print("E → E op E | (E) | num")
    print("op → + | - | * | /")

    # PRUEBA 1 — PRECEDENCIA
    cadena1 = "2 + 3 * 4"

    print("\nPRUEBA 1: CAMBIO DE PRECEDENCIA")
    print("Cadena:", cadena1)

    versiones_prec = [
        ("Precedencia normal (* > +)", {
            "+": (1, "L"),
            "-": (1, "L"),
            "*": (2, "L"),
            "/": (2, "L")
        }),
        ("Precedencia inversa (+ > *)", {
            "+": (2, "L"),
            "-": (2, "L"),
            "*": (1, "L"),
            "/": (1, "L")
        })
    ]

    for nombre, tabla in versiones_prec:
        print("\n", nombre)
        tokens = lexer(cadena1)
        ast = ParserPratt(tokens, tabla).parse_expr()
        print("AST:", ast)
        print("Resultado:", evaluar(ast))
        imprimir(ast)

    # PRUEBA 2 — ASOCIATIVIDAD
    cadena2 = "10 - 5 - 2"

    print("\nPRUEBA 2: CAMBIO DE ASOCIATIVIDAD")
    print("Cadena:", cadena2)

    versiones_asoc = [
        ("Asociatividad izquierda", {
            "+": (1, "L"),
            "-": (1, "L"),
            "*": (2, "L"),
            "/": (2, "L")
        }),
        ("Asociatividad derecha", {
            "+": (1, "R"),
            "-": (1, "R"),
            "*": (2, "L"),
            "/": (2, "L")
        })
    ]

    for nombre, tabla in versiones_asoc:
        print("\n", nombre)
        tokens = lexer(cadena2)
        ast = ParserPratt(tokens, tabla).parse_expr()
        print("AST:", ast)
        print("Resultado:", evaluar(ast))
        imprimir(ast)