# Ejercicio 2 — Comparación CYK vs ANTLR


---

## ¿Qué hace?

Compara dos algoritmos de análisis sintáctico midiendo **tiempo de ejecución (ms)** y **memoria pico (KB)** con el módulo `tracemalloc` de Python, para cadenas de longitud creciente:

| Algoritmo | Complejidad tiempo | Complejidad memoria | Tipo |
|-----------|--------------------|---------------------|------|
| **CYK**   | O(n³ · \|G\|)      | O(n² · \|V\|)       | Bottom-up, cualquier GLC en FNC |
| **ANTLR** | O(n) en práctica   | O(n)                | LL(*),                          |

---

## Gramáticas utilizadas

Para la comparación experimental se usan dos gramáticas distintas pero equivalentes sobre las cadenas generadas de prueba. CYK requiere una gramática en FNC, mientras que ANTLR utiliza una gramática EBNF con precedencia explícita.

### CYK — Forma Normal de Chomsky (FNC)

CYK requiere que todas las producciones sean `A → BC` o `A → a`:

```
S  →  a  |  S A
A  →  OP S
OP →  +  |  -  |  *  |  /
```

### ANTLR — Archivo `Ejercicio2.g4`

ANTLR acepta gramáticas EBNF directamente:

```antlr


grammar Ejercicio2;

s    : expr ;
expr : term (( '+' | '-' ) term)* ;
term : factor (( '*' | '/' ) factor)* ;
factor : 'a' | '(' expr ')' ;
WS   : [ \t\r\n]+ -> skip ;
```

---


## Requisitos

```bash
pip install antlr4-python3-runtime
```

Los archivos generados ya están incluidos en el repositorio. Si se modifica el `.g4`, regenerar con:

```bash
antlr4 -Dlanguage=Python3 Ejercicio2.g4
```

---

## Cómo ejecutar

```bash
cd Ejercicio2/
python3 Ejercicio2.py
```

---

## Resultados obtenidos

| n  | CYK tiempo(ms) | CYK mem(KB) | ANTLR tiempo(ms) | ANTLR mem(KB) |
|----|----------------|-------------|------------------|---------------|
| 2  | 0.0379         | 2.37        | 0.9776           | 147.36        |
| 3  | 0.0695         | 6.05        | 0.2951           | 15.30         |
| 5  | 0.2270         | 18.95       | 0.2554           | 14.17         |
| 8  | 0.8294         | 50.41       | 0.2465           | 13.84         |
| 10 | 1.5717         | 81.12       | 0.2677           | 13.70         |
| 15 | 5.1902         | 186.67      | 0.4271           | 18.29         |
| 20 | 12.6235        | 335.55      | 0.6055           | 23.22         |

**Observaciones:**
- El tiempo CYK se multiplica cada vez que n se duplica (consistente con O(n³)).
- La memoria CYK crece en O(n²): de 18.95 KB (n=5) a 335.55 KB (n=20), factor.


---

## Estructura del código

```
Ejercicio2/
├── Ejercicio2.g4            # Gramática ANTLR (fuente, editable)
├── Ejercicio2.py            # Script principal de comparación
│   ├── def cyk_process()    # Algoritmo CYK: tabla n×n con programación dinámica
│   ├── def generar_cadena() # Genera cadena de prueba de n operandos
│   ├── def medir_cyk()      # Mide tiempo y memoria de CYK
│   └── def medir_antlr()    # Mide tiempo y memoria de ANTLR
├── Ejercicio2Lexer.py       # Generado por ANTLR: tokenizador
├── Ejercicio2Parser.py      # Generado por ANTLR: parser LL(*)
└── Ejercicio2Listener.py    # Generado por ANTLR: patrón Listener (no usado)
```
