# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Model: {self.model}, Any: {self.any}")

# Exemple d'ús
cotxe1 = Cotxe("Toyota", "Corolla", 2020)
cotxe1.mostrar_info()
