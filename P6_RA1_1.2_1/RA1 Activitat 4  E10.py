# Demana a l'usuari que introdueixi dos números
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

# Realitza les operacions bàsiques
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2

# Comprova que la divisió sigui possible (evita la divisió per zero)
if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "No es pot dividir per zero"

# Mostra els resultats
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicació:", multiplicacio)
print("Divisió:", divisio)
