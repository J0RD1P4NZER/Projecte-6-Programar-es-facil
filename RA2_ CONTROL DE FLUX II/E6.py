# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 26/4/2025

fib = [0, 1]
for _ in range(8):
    fib.append(fib[-1] + fib[-2])
print("Seqüència de Fibonacci:", fib)
