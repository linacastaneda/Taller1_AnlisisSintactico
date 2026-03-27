# Ejercicio 1 — Árbol Sintáctico Detallado (ASD)


---

## ¿Qué hace?

Implementa un analizador sintáctico en Python que genera el **árbol de derivación completo (ASD)** para cualquier expresión aritmética. Aunque no es completamente general, respeta la estructura formal de la gramática y permite construir correctamente el árbol de sintaxis.

---
## Enfoque de implementación

El analizador sintáctico se implementó mediante un **enfoque descendente recursivo**, donde cada no terminal de la gramática (`E`, `T`, `F`) se representa como una función específica dentro del parser.

Esta decisión se tomó por las siguientes razones:

- Permite una implementación clara y directa de la gramática dada.
- Facilita la construcción del árbol de sintaxis (ASD) de forma natural durante el análisis.
- Resulta más sencillo de aplicar dada esta gramática.


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


---

### `class Parser`

Contiene toda la lógica del análisis sintáctico descendente recursivo. Recibe la lista de tokens del lexer y construye el ASD siguiendo exactamente la estructura de la gramática.


**Cómo se logra la precedencia sin tabla:** `parse_E` siempre llama a `parse_T` para obtener su operando. Esto significa que todos los `*` se agrupan antes de que `parse_E` pueda usar el resultado como parte de una suma. La jerarquía de llamadas `E → T → F` implementa la precedencia de forma natural.

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
├── GRAMATICA            # Representación formal de la gramática
├── TOKENS               # Mapeo nombre simbólico → símbolo real
├── class NodoASD        # Nodo n-ario del árbol (etiqueta + lista de hijos)
│
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