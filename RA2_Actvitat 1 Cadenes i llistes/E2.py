# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 28/4/2025
# Exercicis de cadenes

frase = input("Introdueix una frase: ").lower()
num_vocals = sum(frase.count(vocal) for vocal in 'aeiou')
print("La frase conté", num_vocals, "vocals.")
