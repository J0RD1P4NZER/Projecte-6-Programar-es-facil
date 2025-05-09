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

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pàgines):
        super().__init__(titol, autor)
        self.n_pàgines = n_pàgines

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pàgines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")

# Creació d'instàncies i prova dels mètodes
llibre_paper = LlibrePaper("El Senyor dels Anells", "J.R.R. Tolkien", 1000)
llibre_digital = LlibreDigital("1984", "George Orwell", "PDF")
