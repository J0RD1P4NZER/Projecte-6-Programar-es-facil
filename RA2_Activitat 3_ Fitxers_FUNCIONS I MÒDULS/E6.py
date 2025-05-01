# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 1/5/2025
# FUNCIONS I MÒDULS

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as fitxer:
        print(fitxer.read())
else:
    print("Error: El fitxer 'dades.txt' no existeix.")
