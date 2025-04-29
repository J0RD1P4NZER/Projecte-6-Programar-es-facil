# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 29/4/2025
# Exercicis de llistes

paraules = input("Introdueix paraules separades per espais: ").split()
vocals = [p for p in paraules if p[0].lower() in "aeiou"]
print("Paraules que comencen per vocal:", vocals)
