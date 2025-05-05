# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5

estudiants = [Estudiant("Anna", 7), Estudiant("Jordi", 4), Estudiant("Marta", 6)]

print("Estudiants que han aprovat:")
for estudiant in estudiants:
    if estudiant.ha_aprovat():
        print(estudiant.nom)
