# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 29/4/2025
# Exercicis de llistes

numeros = [int(input(f"Número {i+1}: ")) for i in range(10)]
parells = [n for n in numeros if n % 2 == 0]
senars = [n for n in numeros if n % 2 != 0]
print("Parells:", parells)
print("Senars:", senars)
