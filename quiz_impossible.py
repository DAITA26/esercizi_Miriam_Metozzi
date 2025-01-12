import random
# dobbiamo fare 3 o 5 domande, ciascuna con 4 opzioni di risposta, le domande le salviamo in una tupla
# le opzioni le salviamo in un dizionario
# per ogni domanda la macchina sceglie a caso una risposta giusta e salva la risposta giusta in una lista
# per ogni domanda viene richiesto all'utente di scegliere una risposta e quella risposta viene salvata in una lista
# per ogni domanda facciamo il confronto tra le due risposte comunicando giusto o sbagliato
# alla fine vogliamo il punteggio

# domande salvate in una tupla
domande = (
"1. Qual'è il nome del mio gatto?",
"2. A quale colore sto pensando?",
"3. Quale genere musicale sto ascoltando?")

# risposte salvate in un dizionario
opz_risposte = {
0: "A: Anubi, B: Simba, C: Romeo, D: Palla di Neve",
1: "A: Magenta, B: Vinaccia, C: Bordeaux, D: Cremisi",
2: "A: Rock, B: Jazz, C: Classica, D: Pop"
}

# variabili globali
punteggio = 0
gioca = True

# risposte del pc e dell'utente salvate in una lista per poi confrontarle
risposte_pc = []
risposte_utente = []

possibili_risposte = ("A", "B", "C", "D")

def chiedi_domande():
    global punteggio

    for i in range(0,len(domande)):
        print(domande[i])
        print(opz_risposte[i])

        scelta_pc = random.choice(possibili_risposte)
        risposte_pc.append(scelta_pc)
        print(scelta_pc)

        scelta_utente = input("Scegli una risposta: ").strip().upper()
        risposte_utente.append(scelta_utente)

        if scelta_pc == scelta_utente:
            print("Hai vinto!")
            punteggio+=1
        else:
            print("Hai perso!")

        print(f"Adesso il tuo punteggio è: {punteggio}")


def vuoi_giocare():
    global gioca
    scelta = input("Vuoi giocare ancora?").strip().lower()
    if scelta == "si":
        gioca = True
    else:
        gioca = False

while gioca:
    chiedi_domande()
    vuoi_giocare()

print(f"Il tuo punteggio finale è: {punteggio}")










