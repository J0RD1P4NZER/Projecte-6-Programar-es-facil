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

class Missatger:
    def enviar(self, missatge):
        pass  # Mètode abstracte

class Email(Missatger):
    def enviar(self, missatge):
        print(f"📧 Enviant email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"📱 Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"💬 Enviant WhatsApp: {missatge}")

def enviar_missatges(missatgers, missatge):
    for missatger in missatgers:
        missatger.enviar(missatge)

# Creació d'instàncies i crida a la funció
missatgers = [Email(), SMS(), WhatsApp()]
enviar_missatges(missatgers, "Hola, com estàs?")