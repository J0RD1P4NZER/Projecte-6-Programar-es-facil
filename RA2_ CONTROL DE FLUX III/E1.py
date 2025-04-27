# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 27/4/2025

try:
    n = int(input("Introdueix un nombre enter: "))
    for i in range(n + 1):
        print(i)
except ValueError:
    print("Error: Has d'introduir un nombre enter.")
