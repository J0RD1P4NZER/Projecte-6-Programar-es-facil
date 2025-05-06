# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self._nota = nota if 0 <= nota <= 10 else 0  # Atribut protegit

    def llegir_nota(self):
        return f"La nota de {self.nom} és: {self._nota}"

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
            print(f"Nota actualitzada a {self._nota}")
        else:
            print("Error: La nota ha de ser entre 0 i 10.")

# Exemple d'ús
estudiant1 = Estudiant("Maria", 7)
print(estudiant1.llegir_nota())

estudiant1.modificar_nota(9)
estudiant1.modificar_nota(11)  # No permet valors fora del rang
