"""Comparativa de algoritmos de análisis: CYK frente a ANTLR.

Este script mide tiempo y memoria en ejecución para cadenas de prueba de longitud variable.
"""

import time
import tracemalloc
import random
from antlr4 import *
from Ejercicio2Lexer import Ejercicio2Lexer
from Ejercicio2Parser import Ejercicio2Parser

# 1. CYK O(n³)

def cyk_process(tokens, gram):
    """Evalúa una cadena de tokens con el algoritmo CYK usando una gramática en FNC.

    Args:
        tokens (list[str]): Lista de símbolos terminales.
        gram (dict): Gramática en forma CNF, por ejemplo {'S': [['A', 'B'], ['a']]}

    Returns:
        bool: True si la cadena pertenece al lenguaje; False en caso contrario.
    """
    n = len(tokens)
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    for i, tok in enumerate(tokens):
        for A, prods in gram.items():
            for p in prods:
                if len(p) == 1 and p[0] == tok:
                    tabla[i][i].add(A)

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for A, prods in gram.items():
                    for p in prods:
                        if len(p) == 2:
                            if p[0] in tabla[i][k] and p[1] in tabla[k+1][j]:
                                tabla[i][j].add(A)

    return "S" in tabla[0][n-1]


# Gramática FNC con + - * /
gram_fnc = {
    "S": [["a"], ["S", "A"]],
    "A": [["OP", "S"]],
    "OP": [["+"], ["-"], ["*"], ["/"]]
}


# 2. GENERADOR DE CADENAS


def generar_cadena(n):
    """Genera una cadena de prueba para benchmarking.

    La cadena alterna el terminal 'a' con operadores aritméticos.

    Args:
        n (int): Número de operandos 'a' que deben generarse.

    Returns:
        tuple: (tokens, cadena), donde tokens es la lista de símbolos y cadena la versión en texto.
    """
    ops = ["+", "-", "*", "/"]
    tokens = []

    for i in range(n):
        if i > 0:
            tokens.append(random.choice(ops))
        tokens.append("a")

    return tokens, " ".join(tokens)


# 3. MEDICIÓN


def medir_cyk(tokens):
    """Mide tiempo y memoria del proceso CYK para una lista de tokens.

    Args:
        tokens (list[str]): Lista de tokens de entrada.

    Returns:
        tuple: (tiempo_ms, memoria_kb).
    """
    tracemalloc.start()
    t0 = time.perf_counter()

    cyk_process(tokens, gram_fnc)

    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return (t1 - t0) * 1000, mem / 1024


def medir_antlr(cadena):
    """Mide tiempo y memoria de análisis ANTLR para una expresión de cadena.

    Args:
        cadena (str): Expresión a parsear con ANTLR.

    Returns:
        tuple: (tiempo_ms, memoria_kb).
    """
    tracemalloc.start()
    t0 = time.perf_counter()

    input_stream = InputStream(cadena)
    lexer = Ejercicio2Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Ejercicio2Parser(tokens)
    parser.s()

    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return (t1 - t0) * 1000, mem / 1024



# 4. MAIN — TABLA


if __name__ == "__main__":
    print("=" * 80)
    print("  EJERCICIO 2 — Comparación CYK vs ANTLR")
    print("=" * 80)
    print()

    print(f"{'n':>5} | {'CYK tiempo(ms)':>16} | {'CYK mem(KB)':>12} | "
          f"{'ANTLR tiempo(ms)':>18} | {'ANTLR mem(KB)':>14}")
    print("-" * 80)

    tamaños = [2, 3, 5, 8, 10, 15, 20]

    for n in tamaños:
        tokens, cadena = generar_cadena(n)

        t_cyk, m_cyk = medir_cyk(tokens)
        t_antlr, m_antlr = medir_antlr(cadena)

        print(f"{n:>5} | {t_cyk:>16.4f} | {m_cyk:>12.2f} | "
              f"{t_antlr:>18.4f} | {m_antlr:>14.2f}")