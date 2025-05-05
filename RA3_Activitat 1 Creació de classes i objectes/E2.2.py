# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

rectangle1 = Rectangle(3, 5)
rectangle2 = Rectangle(7, 2)
rectangle3 = Rectangle(6, 4)

print("Àrea del primer rectangle:", rectangle1.area())
print("Àrea del segon rectangle:", rectangle2.area())
print("Àrea del tercer rectangle:", rectangle3.area())
