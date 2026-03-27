# — Taller 1: Análisis Sintáctico

---

## Descripción general

Este repositorio contiene los tres ejercicios del Taller 1 sobre análisis sintáctico. Cada ejercicio está en su propia carpeta con su código fuente, capturas de ejecución y README individual.

---

## Estructura del repositorio

```
ACTIVIDADAST/
├── Ejercicio1/
│   ├── Ejercicio1.py          # Parser ASD con gramática configurable
│   ├── README.md              # Documentación del ejercicio 1
│   ├── ASD_2p3x4.png          # Árbol generado para 2+3*4
│   ├── ASD_2p3m4.png          # Árbol generado para 2+3-4
│   └── ASD_2p3x(4m5).png      # Árbol generado para 2+3*(4-5)
│
├── Ejercicio2/
│   ├── Ejercicio2.py          # Comparación CYK vs ANTLR con métricas
│   ├── Ejercicio2.g4          # Gramática ANTLR
│   ├── Ejercicio2Lexer.py     # Generado por ANTLR
│   ├── Ejercicio2Parser.py    # Generado por ANTLR
│   ├── README.md              # Documentación del ejercicio 2
│   └── Outputs/               # Capturas de ejecución
│
├── Ejercicio3/
│   ├── Ejercicio3.py          # 4 gramáticas: precedencia y asociatividad
│   ├── README.md              # Documentación del ejercicio 3
│   └── Outputs/               # Capturas de ejecución
│
└── README.md                  # Este archivo
```

---

## Resumen de ejercicios

### Ejercicio 1 — Árbol Sintáctico Detallado (ASD)

Analizador sintáctico descendente recursivo con gramática configurable. Genera el árbol de derivación completo mostrando todos los nodos no-terminales (E, T, F).

**Cadenas de prueba:** `2+3*4` · `2+3-4` · `2+3*(4-5)`  
**Ver:** [Ejercicio1/README.md](Ejercicio1/README.md)

---

### Ejercicio 2 — Comparación CYK vs ANTLR

Comparación de complejidad algorítmica midiendo tiempo (ms) y memoria (KB):

| Algoritmo | Tiempo        | Memoria       |
|-----------|---------------|---------------|
| CYK       | O(n³ · \|G\|) | O(n² · \|V\|) |
| ANTLR LL(*) | O(n) práctica | O(n)        |

Para n=20: CYK tarda ~12.6 ms y usa 335 KB; ANTLR tarda ~0.6 ms y usa 23 KB.  
**Ver:** [Ejercicio2/README.md](Ejercicio2/README.md)

---

### Ejercicio 3 — Precedencia y Asociatividad

Cuatro versiones de la misma gramática aritmética, combinando:

| Versión | Precedencia       | Asociatividad | `2+3*4` | `10-5-2` |
|---------|-------------------|---------------|---------|----------|
| V1      | normal  (* > +)   | Izquierda     | 14 ✓    | 3 ✓      |
| V2      | normal  (* > +)   | Derecha       | 14      | 7        |
| V3      | inversa (+ > *)   | Izquierda     | 20      | 3        |
| V4      | inversa (+ > *)   | Derecha       | 20      | 7        |

**Ver:** [Ejercicio3/README.md](Ejercicio3/README.md)

---

## Requisitos

```bash
python3 --version        # Python 3.8+
pip install graphviz     # Opcional, para imágenes PNG en Ejercicio 1
pip install antlr4-python3-runtime  # Necesario para Ejercicio 2
```