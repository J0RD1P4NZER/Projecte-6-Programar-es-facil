# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 1/5/2025
# FUNCIONS I MÒDULS

try:
    with open("nombres.txt", "r") as fitxer:
        for linea in fitxer:
            try:
                numero = int(linea.strip())
                print(f"Nombre llegit: {numero}")
            except ValueError:
                print(f"Error: '{linea.strip()}' no és un nombre enter vàlid.")
except FileNotFoundError:
    print("Error: El fitxer 'nombres.txt' no existeix.")
