# Ejercicio 1 — Árbol Sintáctico Detallado (ASD)

**Taller 1 — Análisis Sintáctico**  
Lina Castañeda · Universidad Sergio Arboleda · 2026

---

## ¿Qué hace?

Implementa un analizador sintáctico **descendente recursivo** en Python que genera el **árbol de derivación completo (ASD)** para cualquier expresión aritmética. El árbol muestra todos los nodos no-terminales intermedios (E, T, F), no solo los operadores.

La gramática es **completamente configurable**: basta modificar el diccionario `GRAMATICA` al inicio del archivo para cambiar las producciones. El parser y el lexer se adaptan automáticamente.

---

## Gramática configurada

```
E  →  E opsuma T  |  E opresta T  |  T
T  →  T opmul  F  |  F
F  →  pari E pard  |  id  |  num
```

Los nombres simbólicos se mapean a operadores reales en el diccionario `TOKENS`:

| Token     | Símbolo |
|-----------|---------|
| `opsuma`  | `+`     |
| `opresta` | `-`     |
| `opmul`   | `*`     |
| `pari`    | `(`     |
| `pard`    | `)`     |

---

## Clases y funciones

### `class NodoASD`

Representa un nodo dentro del árbol sintáctico. Cada nodo corresponde a un símbolo de la gramática, ya sea un no-terminal (E, T, F) o un terminal (número, operador, identificador).

| Elemento | Descripción |
|----------|-------------|
| `etiqueta` | El texto que se muestra en el nodo: puede ser `"E"`, `"T"`, `"F"`, `"+"`, `"2"`, etc. |
| `hijos` | Lista de nodos hijos. Un nodo puede tener tantos hijos como símbolos tenga la producción que lo generó. |
| `__init__(etiqueta)` | Crea el nodo con su etiqueta y una lista de hijos vacía. |
| `agregar(hijo)` | Añade un nodo hijo a la lista. Se llama una vez por cada símbolo de la producción elegida. |

**Por qué usa lista de hijos y no izq/der:** la gramática tiene producciones con tres símbolos como `E → E opsuma T` (tres hijos: nodo E, operador, nodo T) o `F → pari E pard` (tres hijos: `(`, subárbol E, `)`). Una estructura binaria no alcanza para representar todos los casos.

---

### `class Parser`

Contiene toda la lógica del análisis sintáctico descendente recursivo. Recibe la lista de tokens del lexer y construye el ASD siguiendo exactamente la estructura de la gramática.

| Elemento | Descripción |
|----------|-------------|
| `tokens` | Lista de tuplas `(tipo, valor)` producida por el lexer. |
| `pos` | Índice del token que se está analizando en este momento. Avanza cada vez que se consume un token. |
| `__init__(tokens)` | Inicializa el parser con la lista de tokens y posición en cero. |
| `peek()` | Devuelve el **tipo** del token actual sin avanzar. Se usa para decidir qué producción aplicar sin consumir el token todavía. |
| `consume(tipo)` | Consume el token actual y avanza `pos`. Si se pasa un tipo esperado y el token no coincide, lanza `SyntaxError`. |
| `parse_E()` | Analiza una expresión según `E → T ((+\|-) T)*`. Construye un nodo `"E"` con tres hijos por cada operador encontrado: el subárbol izquierdo ya construido, el operador, y el nuevo subárbol T. El bucle `while` maneja múltiples sumas/restas con asociatividad izquierda. |
| `parse_T()` | Analiza un término según `T → F (* F)*`. Funciona igual que `parse_E` pero para el operador `*`, produciendo nodos `"T"`. La multiplicación tiene mayor precedencia porque `parse_E` llama a `parse_T` antes de mirar sus propios operadores. |
| `parse_F()` | Analiza un factor según `F → (E) \| id \| num`. Si el token actual es `(`, consume el paréntesis de apertura, llama recursivamente a `parse_E`, y consume el `)` de cierre. Si es un número o identificador, crea directamente un nodo hoja. |

**Cómo se logra la precedencia sin tabla:** `parse_E` siempre llama a `parse_T` para obtener su operando. Esto significa que todos los `*` se agrupan antes de que `parse_E` pueda usar el resultado como parte de una suma. La jerarquía de llamadas `E → T → F` implementa la precedencia de forma natural.

---

## Funciones auxiliares

| Función | Descripción |
|---------|-------------|
| `lexer(cadena)` | Convierte la cadena de texto en una lista de tokens `(tipo, valor)`. Reconoce números de varios dígitos, identificadores alfanuméricos, y los cinco operadores. Añade el token `("$", "$")` al final como centinela de fin de entrada. |
| `imprimir_asd(nodo, prefijo, ultimo)` | Imprime el árbol visualmente en consola usando los conectores `├──` y `└──`. El parámetro `ultimo` indica si el nodo es el último hijo de su padre, para elegir el conector correcto y ajustar el prefijo de indentación para los hijos. |
| `dibujar_asd(nodo, dot)` | Genera el árbol como imagen PNG usando Graphviz. Asigna un identificador único a cada nodo con `id(nodo)` para evitar colisiones, y dibuja una arista por cada relación padre-hijo. Solo disponible si `graphviz` está instalado. |

---

## Cómo ejecutar

```bash
python3 Ejercicio1.py
```

Requiere Graphviz para generar imágenes PNG (opcional):

```bash
pip install graphviz
```

---

## Cadenas de prueba

| Expresión      | Descripción |
|----------------|-------------|
| `2+3*4`        | Precedencia: `*` agrupa antes que `+` |
| `2+3-4`        | Asociatividad izquierda con dos operadores del mismo nivel |
| `2+3*(4-5)`    | Paréntesis que fuerzan la evaluación interna primero |

---

## Salida esperada

### `2+3*4`
```
└── E
    ├── F
    │   └── 2
    ├── +
    └── T
        ├── F
        │   └── 3
        ├── *
        └── F
            └── 4
```

### `2+3-4`
```
└── E
    ├── E
    │   ├── F
    │   │   └── 2
    │   ├── +
    │   └── F
    │       └── 3
    ├── -
    └── F
        └── 4
```

### `2+3*(4-5)`
```
└── E
    ├── F → 2
    ├── +
    └── T
        ├── F → 3
        ├── *
        └── F
            ├── (
            ├── E
            │   ├── F → 4
            │   ├── -
            │   └── F → 5
            └── )
```

---

## Capturas de ejecución

Las imágenes PNG generadas por Graphviz están en la carpeta `Ejercicio1/`:

- `ASD_2p3x4.png` — árbol de `2+3*4`
- `ASD_2p3m4.png` — árbol de `2+3-4`
- `ASD_2p3x(4m5).png` — árbol de `2+3*(4-5)`

---

## Estructura del código

```
Ejercicio1.py
├── GRAMATICA            # Dict configurable de producciones
├── TOKENS               # Mapeo nombre simbólico → símbolo real
├── class NodoASD        # Nodo n-ario del árbol (etiqueta + lista de hijos)
│   ├── __init__()       # Crea nodo con etiqueta y lista de hijos vacía
│   └── agregar()        # Añade un hijo a la lista
├── def lexer()          # Tokenizador: texto → lista de (tipo, valor)
├── class Parser         # Analizador sintáctico descendente recursivo
│   ├── __init__()       # Recibe tokens, inicializa pos=0
│   ├── peek()           # Mira el tipo del token actual sin consumirlo
│   ├── consume()        # Consume el token actual y avanza pos
│   ├── parse_E()        # Regla E → T ((+|-) T)*
│   ├── parse_T()        # Regla T → F (* F)*
│   └── parse_F()        # Regla F → (E) | id | num
├── def imprimir_asd()   # Impresión en consola con conectores ├── └──
└── def dibujar_asd()    # Genera imagen PNG con Graphviz (opcional)
```