# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 27/4/2025

def es_primer(num):
    """Comprova si un nombre és primer."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    # Demana a Polnareff que introdueixi un nombre enter positiu
    n = int(input("Polnareff, introdueix un nombre enter positiu: "))

    # Comprova que el nombre sigui vàlid
    if n < 2:
        print("Error: Has d'introduir un nombre igual o més gran que 2.")
    else:
        print(f"Els nombres primers fins a {n} són:")
        for i in range(2, n + 1):
            if es_primer(i):
                print(i)

except ValueError:
    print("Error: Has d'introduir un nombre enter.")
