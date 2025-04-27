# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 27/4/2025

try:
    n = int(input("JoJo: "))
    if n < 0:
        print("Error: JoJo.")
    else:
        for i in range(0, n + 1, 2):
            print(i)
except ValueError:
    print("Error: JoJo.")
