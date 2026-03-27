# 1. GRAMÁTICA 
GRAMATICA = {
    "E": [["E", "opsuma", "T"], ["E", "opresta", "T"], ["T"]],
    "T": [["T", "opmul", "F"], ["F"]],
    "F": [["pari", "E", "pard"], ["id"], ["num"]]
}

TOKENS = {
    "opsuma": "+",
    "opresta": "-",
    "opmul": "*",
    "pari": "(",
    "pard": ")",
    "num": None,
    "id": None,
}

# 2. NODO ASD
class NodoASD:
    """
    Representa un nodo en el Árbol de Sintaxis Abstracta (ASD).
    
    Atributos:
        etiqueta (str): La etiqueta o valor del nodo.
        hijos (list): Lista de nodos hijos.
    """
    def __init__(self, etiqueta):
        """
        Inicializa un nuevo nodo ASD.
        
        Args:
            etiqueta (str): La etiqueta o valor del nodo.
        """
        self.etiqueta = etiqueta
        self.hijos = []

    def agregar(self, hijo):
        """
        Agrega un hijo a este nodo.
        
        Args:
            hijo (NodoASD): El nodo hijo a agregar.
        """
        self.hijos.append(hijo)

# 3. LEXER
def lexer(cadena):
    """
    Analiza léxicamente una cadena de entrada y produce una lista de tokens.
    
    Args:
        cadena (str): La cadena de entrada a analizar.
        
    Returns:
        list: Lista de tuplas (tipo_token, valor)
        
    Raises:
        ValueError: Si se encuentra un carácter inválido en la entrada.
    """
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
            tokens.append(("num", cadena[i:j]))
            i = j

        elif c.isalpha():
            j = i
            while j < len(cadena) and cadena[j].isalnum():
                j += 1
            tokens.append(("id", cadena[i:j]))
            i = j

        elif c == '+':
            tokens.append(("opsuma", "+")); i += 1

        elif c == '-':
            tokens.append(("opresta", "-")); i += 1

        elif c == '*':
            tokens.append(("opmul", "*")); i += 1

        elif c == '(':
            tokens.append(("pari", "(")); i += 1

        elif c == ')':
            tokens.append(("pard", ")")); i += 1

        else:
            raise ValueError(f"Carácter inválido: {c!r}")

    tokens.append(("$", "$"))
    return tokens


# 4. PARSER
class Parser:
    """
    Analizador sintáctico.
    
    Atributos:
        tokens (list): Lista de tokens a analizar.
        pos (int): Posición actual en la lista de tokens.
    """
    def __init__(self, tokens):
        """
        Inicializa el analizador con una lista de tokens.
        
        Args:
            tokens (list): Lista de tuplas (tipo_token, valor).
        """
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        """
        Mira el tipo del token actual sin consumirlo.
        
        Returns:
            str: El tipo del token actual.
        """
        return self.tokens[self.pos][0]

    def consume(self, tipo=None):
        """
        Consume el token actual, opcionalmente verificando su tipo.
        
        Args:
            tipo (str, optional): Tipo esperado del token.
            
        Returns:
            tuple: El token consumido (tipo, valor).
            
        Raises:
            SyntaxError: Si el tipo no coincide con el esperado.
        """
        tok = self.tokens[self.pos]
        if tipo and tok[0] != tipo:
            raise SyntaxError(f"Esperaba {tipo}, encontró {tok}")
        self.pos += 1
        return tok

    # E → T ((+|-) T)*
    def parse_E(self):
        """
        Analiza una expresión (E) según la gramática.
        
        Returns:
            NodoASD: El nodo raíz del subárbol para la expresión.
        """
        nodo = self.parse_T()

        while self.peek() in ("opsuma", "opresta"):
            tok = self.consume()
            op = NodoASD(tok[1])
            derecho = self.parse_T()

            nuevo = NodoASD("E")
            nuevo.agregar(nodo)
            nuevo.agregar(op)
            nuevo.agregar(derecho)

            nodo = nuevo

        return nodo

    # T → F (* F)*
    def parse_T(self):
        """
        Analiza un término (T) según la gramática.
        
        Returns:
            NodoASD: El nodo raíz del subárbol para el término.
        """
        nodo = self.parse_F()

        while self.peek() == "opmul":
            tok = self.consume("opmul")
            op = NodoASD(tok[1])
            derecho = self.parse_F()

            nuevo = NodoASD("T")
            nuevo.agregar(nodo)
            nuevo.agregar(op)
            nuevo.agregar(derecho)

            nodo = nuevo

        return nodo

    def parse_F(self):
        """
        Analiza un factor (F) según la gramática.
        
        Returns:
            NodoASD: El nodo raíz del subárbol para el factor.
            
        Raises:
            SyntaxError: Si no se puede analizar el factor.
        """
        if self.peek() == "pari":
            nodo = NodoASD("F")

            tok1 = self.consume("pari")
            nodo.agregar(NodoASD(tok1[1]))   # "("

            nodo_E = self.parse_E()
            nodo.agregar(nodo_E)

            tok2 = self.consume("pard")
            nodo.agregar(NodoASD(tok2[1]))   # ")"

            return nodo

        elif self.peek() == "num":
            tok = self.consume("num")
            nodo = NodoASD("F")
            nodo.agregar(NodoASD(tok[1]))
            return nodo

        elif self.peek() == "id":
            tok = self.consume("id")
            nodo = NodoASD("F")
            nodo.agregar(NodoASD(tok[1]))
            return nodo

        else:
            raise SyntaxError("Error en F")


# 5. IMPRIMIR ASD
def imprimir_asd(nodo, prefijo="", ultimo=True):
    """
    Imprime el Árbol de Sintaxis Abstracta en formato de árbol textual.
    
    Args:
        nodo (NodoASD): El nodo raíz del árbol a imprimir.
        prefijo (str): Prefijo para la indentación (usado recursivamente).
        ultimo (bool): Indica si este nodo es el último hijo de su padre.
    """
    print(prefijo + ("└── " if ultimo else "├── ") + nodo.etiqueta)
    prefijo += "    " if ultimo else "│   "

    for i, hijo in enumerate(nodo.hijos):
        imprimir_asd(hijo, prefijo, i == len(nodo.hijos) - 1)

# 6. GRAPHVIZ
try:
    from graphviz import Digraph

    def dibujar_asd(nodo, dot=None):

        if dot is None:
            dot = Digraph(format="png")
            dot.attr(rankdir="TB")

        nid = str(id(nodo))
        dot.node(nid, nodo.etiqueta)

        for hijo in nodo.hijos:
            hid = str(id(hijo))
            dot.edge(nid, hid)
            dibujar_asd(hijo, dot)

        return dot

    GRAPHVIZ_OK = True

except ImportError:
    GRAPHVIZ_OK = False

# 7. MAIN
if __name__ == "__main__":
    expresiones = ["2+3*4", "2+3-4", "2+3*(4-5)"]

    for expr in expresiones:
        print("\nExpresión:", expr)
        parser = Parser(lexer(expr))
        raiz = parser.parse_E()

        if parser.peek() != "$":
            raise SyntaxError("Entrada no consumida completamente")

        imprimir_asd(raiz)
        #  GENERAR IMAGEN
        if GRAPHVIZ_OK:
            dot = dibujar_asd(raiz)
            nombre = "ASD_" + expr.replace("+", "p").replace("*", "x").replace("-", "m")
            dot.render(nombre, cleanup=True)
            print(f"Imagen generada: {nombre}.png")

    if not GRAPHVIZ_OK:
        print("\n Instala graphviz: pip install graphviz")