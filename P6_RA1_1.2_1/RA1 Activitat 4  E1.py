import math

PI = 3.1416  # Constant

def calcular_area(radi):
    return PI * radi ** 2  # Funció

radi = float(input("Introdueix el radi: "))  # Línia que llegeix dades de l’usuari
area = calcular_area(radi)  # Variables: radi, area

print("L'àrea del cercle és:", area)  # Línia que mostra el resultat
