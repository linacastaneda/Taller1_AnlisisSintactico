# EJERCICIO 3 — PRECEDENCIA Y ASOCIATIVIDAD
#
# Gramatica base (configurable via tabla de precedencia):
#   E -> E op E | (E) | num
#   op -> + | - | * | /
#
# Se muestran 4 versiones con la MISMA cadena de entrada
# para observar como cambia el arbol y el resultado:
#
#   V1: Precedencia normal  (* > +),  Asociatividad IZQUIERDA
#   V2: Precedencia normal  (* > +),  Asociatividad DERECHA
#   V3: Precedencia inversa (+ > *),  Asociatividad IZQUIERDA
#   V4: Precedencia inversa (+ > *),  Asociatividad DERECHA


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
    """
    Parser Pratt con binding powers (esquema Matklad).

    Para cada operador se define (nivel, asociatividad):
      - nivel: jerarquia de precedencia (mayor = agrupa antes)
      - asociatividad: 'L' izquierda, 'R' derecha

    Binding powers internos:
      Izquierda (L): lbp = nivel*10,     rbp = nivel*10 + 1
      Derecha   (R): lbp = nivel*10 + 1, rbp = nivel*10

    La regla de parada es: lbp < min_bp -> salir del bucle.
    """
    def __init__(self, tokens, prec):
        self.tokens = tokens
        self.pos = 0
        self.prec = prec  # {op: (nivel, 'L'|'R')}

    def peek(self):
        return self.tokens[self.pos]

    def consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def binding(self, op):
        """Retorna (lbp, rbp) del operador, o (None, None) si no es operador."""
        if op not in self.prec:
            return None, None
        nivel, asoc = self.prec[op]
        base = nivel * 10
        if asoc == 'L':
            return base, base + 1   # rbp > lbp -> agrupa a la izquierda
        else:
            return base + 1, base   # rbp < lbp -> agrupa a la derecha

    def parse_expr(self, min_bp=0):
        lhs = self.parse_primary()
        while True:
            op = self.peek()
            lbp, rbp = self.binding(op)
            if lbp is None or lbp < min_bp:
                break
            self.consume()
            rhs = self.parse_expr(rbp)
            lhs = Nodo(op, lhs, rhs)
        return lhs

    def parse_primary(self):
        tok = self.peek()
        if tok == "(":
            self.consume()
            nodo = self.parse_expr(0)
            self.consume()  # ")"
            return nodo
        if tok.lstrip('-').isdigit():
            return Nodo(int(self.consume()))
        raise SyntaxError(f"Token inesperado: {tok!r}")


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
        imprimir(h, pref + ("    " if ult else "│   "), i == len(hijos) - 1)


# ─────────────────────────────────────────────────────────────
# TABLAS DE PRECEDENCIA — 4 versiones
# ─────────────────────────────────────────────────────────────

# V1: * > +,  Asociatividad IZQUIERDA  (estandar matematico)
PREC_V1 = {"+": (1, "L"), "-": (1, "L"), "*": (2, "L"), "/": (2, "L")}

# V2: * > +,  Asociatividad DERECHA
PREC_V2 = {"+": (1, "R"), "-": (1, "R"), "*": (2, "R"), "/": (2, "R")}

# V3: + > *,  Asociatividad IZQUIERDA  (precedencia invertida)
PREC_V3 = {"+": (2, "L"), "-": (2, "L"), "*": (1, "L"), "/": (1, "L")}

# V4: + > *,  Asociatividad DERECHA    (precedencia invertida + asoc derecha)
PREC_V4 = {"+": (2, "R"), "-": (2, "R"), "*": (1, "R"), "/": (1, "R")}

VERSIONES = [
    ("V1 - Precedencia normal  (* > +),  Asociatividad IZQUIERDA", PREC_V1),
    ("V2 - Precedencia normal  (* > +),  Asociatividad DERECHA",   PREC_V2),
    ("V3 - Precedencia inversa (+ > *),  Asociatividad IZQUIERDA", PREC_V3),
    ("V4 - Precedencia inversa (+ > *),  Asociatividad DERECHA",   PREC_V4),
]


if __name__ == "__main__":
    print("GRAMATICA:")
    print("  E -> E op E | (E) | num")
    print("  op -> + | - | * | /")

    # ── Cadena de prueba 1 ──────────────────────────────────
    cadena1 = "2 + 3 * 4"
    print(f"\n{'='*62}")
    print(f"PRUEBA 1 - Cadena: {cadena1!r}")
    print(f"{'='*62}")

    for nombre, tabla in VERSIONES:
        print(f"\n  {nombre}")
        print(f"  {'-'*58}")
        ast = ParserPratt(lexer(cadena1), tabla).parse_expr()
        print(f"  ASD:       {ast}")
        print(f"  Resultado: {evaluar(ast)}")
        imprimir(ast, pref="  ")

    # ── Cadena de prueba 2 ──────────────────────────────────
    cadena2 = "10 - 5 - 2"
    print(f"\n{'='*62}")
    print(f"PRUEBA 2 - Cadena: {cadena2!r}")
    print(f"{'='*62}")

    for nombre, tabla in VERSIONES:
        print(f"\n  {nombre}")
        print(f"  {'-'*58}")
        ast = ParserPratt(lexer(cadena2), tabla).parse_expr()
        print(f"  ASD:       {ast}")
        print(f"  Resultado: {evaluar(ast)}")
        imprimir(ast, pref="  ")