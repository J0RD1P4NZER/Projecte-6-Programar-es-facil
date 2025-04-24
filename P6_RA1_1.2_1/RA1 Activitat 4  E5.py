# Definim una constant
TAXA_IVA = 0.21  

# Definim una funció que calcula el preu amb IVA
def calcular_preu_amb_iva(preu):
    return preu + (preu * TAXA_IVA)

# Demanem a l'usuari que introdueixi un preu
preu_sense_iva = float(input("Introdueix el preu del producte sense IVA: "))

# Calcula el preu final amb IVA
preu_final = calcular_preu_amb_iva(preu_sense_iva)

# Mostra el resultat per pantalla
print("El preu final amb IVA és:", preu_final)
