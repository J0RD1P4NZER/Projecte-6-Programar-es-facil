# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 27/4/2025

try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n < 1:
        print("Error: El nombre ha de ser positiu.")
    else:
        print("La suma és:", sum(range(1, n + 1)))
except ValueError:
    print("Error: Has d'introduir un nombre enter.")
