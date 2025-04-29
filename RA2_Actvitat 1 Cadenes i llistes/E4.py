# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 28/4/2025
# Exercicis de cadenes

paraula = input("Introdueix una paraula: ").lower()
if paraula == paraula[::-1]:
    print("És un palíndrom.")
else:
    print("No és un palíndrom.")
