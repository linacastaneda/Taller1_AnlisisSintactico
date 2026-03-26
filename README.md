# Taller 1 — Análisis Sintáctico

---

## Descripción

Este repositorio contiene los tres ejercicios del Taller 1 sobre análisis sintáctico.

---

## Ejercicio 1 — Árbol Sintáctico Detallado (ASD)

**Archivo:** `Ejercicio1_ASD.py`

Implementa un analizador sintáctico descendente recursivo que genera el árbol de derivación completo (ASD) para la gramática de expresiones aritméticas de las diapositivas:

```
E  →  E opsuma T  |  T
T  →  T opmul  F  |  F
F  →  pari E pard  |  id  |  num
```

**Características:**
- La gramática es configurable: basta modificar el diccionario `GRAMATICA` y `TOKENS` para cambiar los operadores o las producciones.
- Genera la imagen PNG del árbol si Graphviz está instalado.
- Soporta identificadores (`id`), números (`num`) y paréntesis.

**Ejecución:**
```bash
python3 Ejercicio1_ASD.py
```

**Salida para `2 + 3 * 4`:**
```
└── E
    ├── E
    │   └── T
    │       └── F
    │           └── 2
    ├── +
    └── T
        ├── T
        │   └── F
        │       └── 3
        ├── *
        └── F
            └── 4
```

---

## Ejercicio 2 — Comparación CYK O(n³) vs LL(1) O(n)

**Archivo:** `Ejercicio2_CYK_vs_LL1.py`

Compara el algoritmo CYK (Cocke–Younger–Kasami) con un parser LL(1) descendente recursivo, midiendo tiempo de ejecución (ms) y memoria pico (KB) con `tracemalloc`.

    n |   CYK tiempo(ms) |  CYK mem(KB) |   LL1 tiempo(ms) |  LL1 mem(KB)
--------------------------------------------------------------------------
    2 |           0.1462 |         2.28 |           0.0288 |         0.52
    3 |           0.2812 |         5.88 |           0.0260 |         0.55
    5 |           1.4511 |        18.61 |           0.0125 |         0.61
    8 |           4.6462 |        50.17 |           0.0185 |         0.61
   10 |           9.6093 |        80.72 |           0.0191 |         0.67 
   15 |          35.9956 |       185.94 |           0.0237 |         0.73 
   20 |          86.2134 |       334.70 |           0.0290 |         0.86 

**Complejidades:**

| Algoritmo | Tiempo        | Memoria         |
|-----------|---------------|-----------------|
| CYK       | O(n³ · \|G\|) | O(n² · \|V\|)   |
| LL(1)     | O(n)          | O(n)            |

**Ejecución:**
```bash
python3 Ejercicio2_CYK_vs_LL1.py
```

---

## Ejercicio 3 — Precedencia y Asociatividad

**Archivo:** `Ejercicio3_Precedencia_Asociatividad.py`

Implementa un parser con tabla de precedencia configurable. Se definen cuatro versiones y se compara el árbol AST generado para la misma cadena:

| Versión | Precedencia | Asociatividad |
|---------|-------------|---------------|
| V1      | `* > +`     | Izquierda     |
| V2      | `+ > *`     | Izquierda     |
| V3      | `* > +`     | Derecha       |
| V4      | `+ > *`     | Derecha       |

**Para `2 + 3 * 4`:**
- **V1** → `2 + (3 * 4)` = 14   estándar matemático
- **V2** → `(2 + 3) * 4` = 20  (suma primero)
- **V3** → `2 + (3 * 4)` = 14  (misma prec, asoc derecha no cambia con un solo operador por nivel)
- **V4** → `(2 + 3) * 4` = 20  (suma primero + agrupación derecha)

**Ejecución:**
```bash
python3 Ejercicio3_Precedencia_Asociatividad.py
```

---

## Requisitos

```bash
pip install graphviz   # opcional, solo para generar imágenes PNG en Ej1
python3 --version      # Python 3.8+
```

---

## Estructura del repositorio

```
Taller1_AnálisisSintáctico/
├── Ejercicio1_ASD.py
├── Ejercicio2_CYK_vs_LL1.py
├── Ejercicio3_Precedencia_Asociatividad.py
├── Informe_AnálisisSintáctico.docx
└── README.md
```