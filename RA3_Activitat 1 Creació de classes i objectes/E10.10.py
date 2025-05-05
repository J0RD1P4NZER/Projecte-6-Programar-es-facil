# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

def mostrar_persones_majors(persones):
    print("Persones majors de 30 anys:")
    for persona in persones:
        if persona.edat > 30:
            print(persona.nom)

persones = [Persona("Jordi", 35), Persona("Anna", 25), Persona("Miquel", 40)]
mostrar_persones_majors(persones)
