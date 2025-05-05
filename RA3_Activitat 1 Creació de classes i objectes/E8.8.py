# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}")

class Biblioteca:
    def __init__(self):
        self.llistes_llibres = []

    def afegir_llibre(self, llibre):
        self.llistes_llibres.append(llibre)

    def mostrar_llibres(self):
        print("Llibres a la biblioteca:")
        for llibre in self.llistes_llibres:
            llibre.mostrar_info()

biblioteca = Biblioteca()
biblioteca.afegir_llibre(Llibre("1984", "George Orwell", 1949))
biblioteca.afegir_llibre(Llibre("El Quixot", "Miguel de Cervantes", 1605))
biblioteca.mostrar_llibres()
