# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

import re

class CompteUsuari:
    def __init__(self, email):
        if self.__validar_email(email):
            self.__email = email
        else:
            raise ValueError("Error: L'email ha de contenir '@' i '.'")

    def __validar_email(self, email):
        return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if self.__validar_email(nou_email):
            self.__email = nou_email
        else:
            print("Error: L'email introduït no és vàlid.")

# Exemple d'ús
usuari = CompteUsuari("exemple@gmail.com")
print("Email:", usuari.email)

usuari.email = "nou_email@domini.com"
print("Email actualitzat:", usuari.email)

usuari.email = "email_incorrecte"  # No permet emails invàlids
