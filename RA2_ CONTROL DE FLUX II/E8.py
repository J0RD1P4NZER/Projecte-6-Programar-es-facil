# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 26/4/2025

frase = input("Introdueix una frase: ").lower()
num_vocals = sum(frase.count(vocal) for vocal in 'aeiou')
print("La frase conté", num_vocals, "vocals.")
