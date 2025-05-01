# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 1/5/2025
# FUNCIONS I MÒDULS

with open("sortida.txt", "r+") as fitxer:
    print("Contingut original:")
    print(fitxer.read())
    
    fitxer.write("\nNova línia afegida al final.")
