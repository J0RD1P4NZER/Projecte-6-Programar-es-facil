# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 25/4/2025

# Versió: 1.0

from datetime import date

any_naixement = int(input("Introdueix el teu any de naixement: "))
any_actual = date.today().year
edat = any_actual - any_naixement

print("Tens", edat, "anys.")
if edat >= 18:
    print("Ets major d’edat.")
else:
    print("No ets major d’edat.")
