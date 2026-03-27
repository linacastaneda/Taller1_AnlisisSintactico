# Ejercicio 3 — Precedencia y Asociatividad

**Taller 1 — Análisis Sintáctico**  
Lina Castañeda · Universidad Sergio Arboleda · 2026

---

## ¿Qué hace?

Implementa cuatro versiones de una gramática aritmética, cada una con una combinación distinta de **precedencia de operadores** y **asociatividad**. Se aplica la misma cadena de entrada a las cuatro versiones y se comparan los árboles AST y los valores obtenidos, demostrando cómo estas dos propiedades de la gramática determinan completamente la estructura del árbol de análisis.

---

## Gramática base

```
E  →  E op E  |  (E)  |  num
op →  +  |  -  |  *  |  /
```

La diferencia entre las cuatro versiones está en la **tabla de precedencia** que configura el parser.

---

## Las cuatro gramáticas

| Versión | Precedencia       | Asociatividad | `2+3*4` | `10-5-2` |
|---------|-------------------|---------------|---------|----------|
| V1      | normal  (* > +)   | Izquierda     | 14 ✓    | 3 ✓      |
| V2      | normal  (* > +)   | Derecha       | 14      | 7        |
| V3      | inversa (+ > *)   | Izquierda     | 20      | 3        |
| V4      | inversa (+ > *)   | Derecha       | 20      | 7        |

```python
PREC_V1 = {'+': (1,'L'), '-': (1,'L'), '*': (2,'L'), '/': (2,'L')}
PREC_V2 = {'+': (1,'R'), '-': (1,'R'), '*': (2,'R'), '/': (2,'R')}
PREC_V3 = {'+': (2,'L'), '-': (2,'L'), '*': (1,'L'), '/': (1,'L')}
PREC_V4 = {'+': (2,'R'), '-': (2,'R'), '*': (1,'R'), '/': (1,'R')}
```

---

## Clases y funciones

### `class Nodo`

Representa un nodo en el árbol de sintaxis abstracta (AST). A diferencia del ASD del Ejercicio 1, aquí el árbol es **binario**: cada operador tiene exactamente un hijo izquierdo y uno derecho, y los nodos hoja son números.

| Elemento | Descripción |
|----------|-------------|
| `valor` | El contenido del nodo: un operador (`"+"`, `"-"`, `"*"`, `"/"`) o un número entero. |
| `izq` | Hijo izquierdo: el operando izquierdo de la operación, o `None` si el nodo es una hoja. |
| `der` | Hijo derecho: el operando derecho de la operación, o `None` si el nodo es una hoja. |
| `__init__(valor, izq, der)` | Crea el nodo. Para nodos hoja (números) se omiten `izq` y `der`, que quedan en `None`. |
| `__repr__()` | Devuelve una representación en texto con paréntesis completos. Por ejemplo, `(2 + (3 * 4))`. Los paréntesis rodean cada operación, lo que permite ver exactamente cómo se agrupó la expresión y verificar que la precedencia y asociatividad funcionaron correctamente. |

**Por qué es binario aquí y n-ario en el Ejercicio 1:** el AST (árbol de sintaxis *abstracta*) omite los nodos gramaticales intermedios (E, T, F) y representa directamente la semántica: cada operador binario tiene exactamente dos operandos. El ASD (árbol *detallado*) del Ejercicio 1 sí necesita representar producciones con tres o más símbolos.

---

### `class ParserPratt`

Implementa el algoritmo **Pratt parser** con el esquema de binding powers. Es el núcleo del ejercicio: al cambiar la tabla de precedencia que recibe, produce árboles completamente distintos para la misma entrada.

| Elemento | Descripción |
|----------|-------------|
| `tokens` | Lista de tokens producida por el lexer. |
| `pos` | Posición actual en la lista de tokens. |
| `prec` | Tabla de precedencia: diccionario `{operador: (nivel, asociatividad)}` que define el comportamiento del parser. Es el único parámetro que cambia entre las cuatro versiones. |
| `__init__(tokens, prec)` | Inicializa el parser con los tokens y la tabla de precedencia. La tabla se pasa como parámetro para que el mismo parser pueda ser reutilizado con las cuatro configuraciones. |
| `peek()` | Devuelve el token actual sin consumirlo. Se usa para decidir si el operador siguiente tiene suficiente precedencia para ser consumido en el contexto actual. |
| `consume()` | Consume el token actual y avanza `pos`. Se llama cuando ya se decidió que el operador sí debe ser consumido. |
| `binding(op)` | **Método clave.** Calcula los binding powers del operador: `lbp` (left binding power, qué tan fuerte atrae hacia la izquierda) y `rbp` (right binding power, qué tan fuerte atrae hacia la derecha). La fórmula es: para asociatividad izquierda `lbp = nivel×10, rbp = nivel×10+1` (rbp > lbp, así que el mismo operador no puede continuar hacia la derecha → agrupa izquierda); para asociatividad derecha `lbp = nivel×10+1, rbp = nivel×10` (rbp < lbp, así que el mismo operador sí puede continuar hacia la derecha → agrupa derecha). |
| `parse_expr(min_bp)` | Analiza una expresión completa. Obtiene el operando izquierdo con `parse_primary`, luego entra en un bucle: mientras el `lbp` del operador actual sea mayor o igual a `min_bp`, lo consume y obtiene el operando derecho llamando recursivamente a `parse_expr(rbp)`. El valor de `rbp` controla si el mismo operador puede aparecer en el subárbol derecho, que es exactamente lo que implementa la asociatividad. |
| `parse_primary()` | Analiza un operando primario: si es `(`, consume y llama recursivamente a `parse_expr(0)` y luego consume `)`. Si es un número, crea directamente un nodo hoja `Nodo(int(tok))`. |

**Cómo funciona el control de asociatividad con binding powers:**  
Para el operador `-` con asociatividad izquierda (nivel=1): `lbp=10, rbp=11`.  
- En `10 - 5 - 2`: se procesa `10`, se ve `-` con `lbp=10 >= min_bp=0` → se consume, se llama `parse_expr(rbp=11)`.  
- En la recursión, el siguiente `-` tiene `lbp=10 < min_bp=11` → no se consume → la recursión retorna solo `5`.  
- Resultado: el primer `-` queda con `izq=10` y `der=5`, formando `(10-5)`. Luego el segundo `-` se procesa a nivel superior con `izq=(10-5)` y `der=2` → `((10-5)-2)`.

---

## Funciones auxiliares

| Función | Descripción |
|---------|-------------|
| `lexer(cadena)` | Convierte la cadena de texto en lista de tokens. Reconoce números de varios dígitos y los cuatro operadores. Añade `"$"` como centinela de fin de entrada. |
| `evaluar(n)` | Recorre el árbol AST recursivamente y calcula el valor numérico de la expresión. En los nodos hoja devuelve `n.valor` directamente. En los nodos internos, llama recursivamente a `evaluar(n.izq)` y `evaluar(n.der)` y aplica el operador del nodo raíz. Permite verificar que el árbol generado por cada gramática produce el resultado aritmético correcto. |
| `imprimir(n, pref, ult)` | Imprime el árbol AST en consola con conectores visuales `├──` y `└──`. Funciona igual que `imprimir_asd` del Ejercicio 1, pero el árbol siempre es binario (máximo dos hijos por nodo). |

---

## Cómo ejecutar

```bash
python3 Ejercicio3.py
```

---

## Resultados

### Prueba 1 — `2 + 3 * 4` (efecto de la precedencia)

```
V1 (* > +, izq):  AST: (2 + (3 * 4))   Resultado: 14  <- estándar
V2 (* > +, der):  AST: (2 + (3 * 4))   Resultado: 14
V3 (+ > *, izq):  AST: ((2 + 3) * 4)   Resultado: 20  <- suma primero
V4 (+ > *, der):  AST: ((2 + 3) * 4)   Resultado: 20
```

Con un solo operador de cada tipo, la asociatividad no cambia el resultado. Lo que distingue es la **precedencia**.

### Prueba 2 — `10 - 5 - 2` (efecto de la asociatividad)

```
V1 (* > +, izq):  AST: ((10 - 5) - 2)   Resultado:  3  <- estándar
V2 (* > +, der):  AST: (10 - (5 - 2))   Resultado:  7
V3 (+ > *, izq):  AST: ((10 - 5) - 2)   Resultado:  3
V4 (+ > *, der):  AST: (10 - (5 - 2))   Resultado:  7
```

Con un solo tipo de operador, la precedencia no distingue. Lo que cambia es la **asociatividad**.

---

## Capturas de ejecución

**Prueba 1 — cambio de precedencia:**

![Captura 1](Outputs/Salida1.png)

**Prueba 2 — cambio de asociatividad:**

![Captura 2](Outputs/Salida2.png)

---

## Estructura del código

```
Ejercicio3.py
├── PREC_V1 / V2 / V3 / V4  # Las 4 tablas de precedencia configurables
├── class Nodo               # Nodo binario del AST (valor + izq + der)
│   ├── __init__()           # Crea nodo con valor e hijos opcionales
│   └── __repr__()           # Representación con paréntesis: (izq op der)
├── def lexer()              # Tokenizador: texto → lista de tokens
├── class ParserPratt        # Parser Pratt con binding powers
│   ├── __init__()           # Recibe tokens y tabla de precedencia
│   ├── peek()               # Mira el token actual sin consumirlo
│   ├── consume()            # Consume el token actual y avanza pos
│   ├── binding()            # Calcula lbp y rbp según nivel y asociatividad
│   ├── parse_expr()         # Bucle principal: consume operadores por precedencia
│   └── parse_primary()      # Analiza paréntesis o número
├── def evaluar()            # Evalúa el AST numéricamente de forma recursiva
└── def imprimir()           # Imprime el árbol con conectores ├── └──
```