# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 1/5/2025
# FUNCIONS I MÒDULS

try:
    with open("nou_fitxer.txt", "r") as fitxer:
        print("El fitxer ja existeix. Contingut:")
        print(fitxer.read())
except FileNotFoundError:
    with open("nou_fitxer.txt", "w") as fitxer:
        fitxer.write("Fitxer creat automàticament.\n")
    print("S'ha creat 'nou_fitxer.txt' amb un missatge per defecte.")
