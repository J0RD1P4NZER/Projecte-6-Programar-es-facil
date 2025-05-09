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

class EmailNotificador:
    def enviar(self, missatge):
        print(f"📧 Enviant email: {missatge}")

class SMSNotificador:
    def enviar(self, missatge):
        print(f"📱 Enviant SMS: {missatge}")

class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador  # Dependència injectada

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")

# Ús amb diferents tipus de notificadors
comanda_email = Comanda("Daniel", EmailNotificador())
comanda_email.confirmar()

comanda_sms = Comanda("Daniel", SMSNotificador())
comanda_sms.confirmar()