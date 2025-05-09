# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 9/5/2025
# Versió: 1.0
# ************************************************************
# Descripció: 
# Factura i impressora: Genera i imprimeix una factura amb una impressora configurable.
# Especificacions d'entrada:
# 
# ************************************************************

class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class ImpressoraText:
    def imprimir(self, contingut):
        print(f"Imprimint en text: {contingut}")

class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Dependència injectada

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)

# Ús amb diferents tipus d'impressores
factura_pdf = Factura("Daniel", 100, ImpressoraPDF())
factura_pdf.imprimir_factura()

factura_text = Factura("Daniel", 100, ImpressoraText())
factura_text.imprimir_factura()