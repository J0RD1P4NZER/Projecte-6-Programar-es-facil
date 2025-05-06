# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Usuari:
    def __init__(self, contrasenya):
        if len(contrasenya) >= 8:
            self.__contrasenya = contrasenya
        else:
            raise ValueError("Error: La contrasenya ha de tenir almenys 8 caràcters.")

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            print("Contrasenya actualitzada correctament.")
        else:
            print("Error: La contrasenya ha de tenir almenys 8 caràcters.")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau

# Exemple d'ús
usuari1 = Usuari("password123")
print("Verificació:", usuari1.verificar_contrasenya("password123"))

usuari1.canviar_contrasenya("novaContrasenyaSegura")
print("Verificació després del canvi:", usuari1.verificar_contrasenya("novaContrasenyaSegura"))
