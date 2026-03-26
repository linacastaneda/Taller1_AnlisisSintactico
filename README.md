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

## Ejercicio 2 — Comparación CYK O(n³) vs LL(1) O(n)

**Archivo:** `Ejercicio2_CYK_vs_LL1.py`

Compara el algoritmo CYK (Cocke–Younger–Kasami) con un parser LL(1) descendente recursivo, midiendo tiempo de ejecución (ms) y memoria pico (KB) con `tracemalloc`.

    n |   CYK tiempo(ms) |  CYK mem(KB) |   ANTLR tiempo(ms) |  ANTLR mem(KB)
--------------------------------------------------------------------------------
    2 |           0.0323 |         2.20 |             0.9225 |         146.71
    3 |           0.0647 |         5.83 |             0.2393 |          12.73
    5 |           0.2007 |        18.95 |             0.2272 |          13.74
    8 |           0.7715 |        50.41 |             0.3055 |          15.38
   10 |           1.5043 |        81.06 |             0.2772 |          14.29
   15 |           5.0912 |       186.61 |             0.4229 |          19.15
   20 |          12.0687 |       335.59 |             0.5593 |          23.38

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