import time
import sys
from lark import Lark

# 1. Implementación del Algoritmo CYK (O(n^3))
def cyk_parse(cadena, gramatica):
    n = len(cadena)
    if n == 0: return False
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Paso 1: Terminales
    for i in range(n):
        for var, prods in gramatica.items():
            if cadena[i] in prods:
                tabla[i][i].add(var)

    # Paso 2: Producciones Binarias
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for var, prods in gramatica.items():
                    for p in prods:
                        if isinstance(p, tuple) and p[0] in tabla[i][k] and p[1] in tabla[k+1][j]:
                            tabla[i][j].add(var)
    return "S" in tabla[0][n-1]

# Gramática en Formato Chomsky para CYK
gramatica_chomsky = {
    "S": [("A", "B"), "a"],
    "A": ["a"],
    "B": [("O", "A"), ("O", "B")],
    "O": ["+", "*"]
}

# 2. Configuración de Motor tipo BISON (LALR - O(n))
grammar_bison = """
    ?start: expr
    ?expr: term (("+" | "*") term)*
    ?term: "a"
    %import common.WS
    %ignore WS
"""
parser_bison = Lark(grammar_bison, parser='lalr')

def benchmark():
    # Probamos con cadenas de longitud creciente: 10, 50, 100, 200 tokens
    escalas = [10, 50, 100, 150]
    
    print(f"{'Tokens':<10} | {'Tiempo CYK (s)':<18} | {'Tiempo BISON (s)':<18}")
    print("-" * 55)

    for n in escalas:
        # Generamos una cadena larga: a+a*a+a...
        cadena = "a" + "+a" * (n // 2)
        
        # Medir CYK
        start = time.time()
        cyk_parse(cadena, gramatica_chomsky)
        t_cyk = time.time() - start

        # Medir Bison (LALR)
        start = time.time()
        parser_bison.parse(cadena)
        t_bison = time.time() - start

        print(f"{n:<10} | {t_cyk:<18.6f} | {t_bison:<18.6f}")

if __name__ == "__main__":
    benchmark()
