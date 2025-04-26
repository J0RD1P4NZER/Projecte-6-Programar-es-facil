# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 26/4/2025

import random

num_secret = random.randint(1, 100)
while True:
    intent = int(input("Endevina el número (entre 1 i 100): "))
    if intent < num_secret:
        print("Massa baix.")
    elif intent > num_secret:
        print("Massa alt.")
    else:
        print("Correcte!")
        break
