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

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")

# Creació d'una instància de Treballador i prova dels mètodes
treballador = Treballador("Daniel", 30, "Enginyer informàtic")
treballador.saludar()
treballador.mostrar_feina()