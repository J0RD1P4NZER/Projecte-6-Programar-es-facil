# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 1/5/2025
# FUNCIONS I MÒDULS

try:
    with open("resultats.txt", "w") as fitxer:
        fitxer.write("Aquest text s'està escrivint en resultats.txt.\n")
except PermissionError:
    print("Error: No tens permisos per escriure en aquest fitxer.")
