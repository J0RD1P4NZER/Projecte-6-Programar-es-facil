# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 1/5/2025
# FUNCIONS I MÒDULS

try:
    fitxer = open("error_fitxer.txt", "r")
    contingut = fitxer.read()
    print(contingut)
finally:
    fitxer.close()
    print("El fitxer s'ha tancat correctament.")
