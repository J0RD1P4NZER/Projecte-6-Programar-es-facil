# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 9/5/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

class Figura:
    def dibuixar(self):
        pass  # Mètode abstracte

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle ◯")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat ⬛")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle 🔺")

# Creació d'una llista de figures
figures = [Cercle(), Quadrat(), Triangle()]

# Recórrer la llista i cridar dibuixar()
for figura in figures:
    figura.dibuixar()