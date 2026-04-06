# Tarea2-Analisis_sintactico


Este proyecto analiza la eficiencia algorítmica de dos enfoques de parsing: el algoritmo académico **CYK** frente al estándar industrial **Bison (LALR)**.

## Metodología del Benchmark
Se comparan dos algoritmos con complejidades computacionales muy distintas:
1. **CYK (Cocke-Younger-Kasami):** Un algoritmo de programación dinámica con una complejidad de **$O(n^3)$**.
2. **Bison (Representado por LALR):** Un algoritmo de análisis ascendente de un solo paso con complejidad **$O(n)$**.

## Cómo ejecutar
1. Instalar dependencias:
   ```bash
   pip install lark --break-system-packages
   ```
2. Correr el benchmark:
  ```bash
    python analizador_benchmark.py
  ```
