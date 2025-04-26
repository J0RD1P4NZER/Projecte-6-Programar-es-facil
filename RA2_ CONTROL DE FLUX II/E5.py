# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 26/4/2025

num = int(input("Introdueix un número positiu: "))
es_primer = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

if es_primer:
    print(f"{num} és un nombre primer.")
else:
    print(f"{num} no és un nombre primer.")
