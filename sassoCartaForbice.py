import random

print("Benvenuto a morra cinese!")

continua = True

while continua:
    scelta = input("Scegli tra sasso, carta e forbice: ").lower().strip()

    if scelta != "sasso" and scelta != "carta" and scelta != "forbice":
        print("Scelta non valida")
        continue

    sceltaComputer = random.randint(1, 3)

    if sceltaComputer == 1:
        sceltaComputer = "sasso"
    elif sceltaComputer == 2:
        sceltaComputer = "carta"
    else:
        sceltaComputer = "forbice"

    print(f"La scelta del pc è {sceltaComputer}")

    if scelta == sceltaComputer:
        print("Pareggio!")
    elif scelta == "sasso" and sceltaComputer == "forbice":
        print("Hai vinto!")
    elif scelta == "carta" and sceltaComputer == "sasso":
        print("Hai vinto!")
    elif scelta == "forbice" and sceltaComputer == "carta":
        print("Hai vinto!")
    else:
        print("Hai perso!")

    while True:
        continua = input("Vuoi continuare a giocare? ").strip().lower()

        if continua == "si":
            continua = True
            break

        elif continua == "no":
            continua = False
            break

        else:
            print("Risposta non valida. Scegli tra 'si' o 'no'.")

