# gestione cognome e nome
class StringaDiTesto:
    def __init__(self, stringa):
        self.stringa = stringa.upper()

    def separatrice(self):
        vocali_alf = "AEIOU"
        consonanti = ""
        vocali = ""
        for c in self.stringa:
            if c.isalpha():
                if c in vocali_alf:
                    vocali += c
                else:
                    consonanti += c
        return consonanti, vocali

    def risStringa(self, tipo="nome"):
        consonanti, vocali = self.separatrice()
        if tipo == "nome" and len(consonanti) >= 4:
            return consonanti[0] + consonanti[2] + consonanti[3]
        return (consonanti + vocali + "XXX")[:3]  # prende solo i primi 3 caratteri



# gestione data di nascita
class DataDiNascita:
    def __init__(self, data, sesso):
        self.data = data
        self.sesso = sesso.upper()
        giorni_mesi = {
            "01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "H",
            "07": "L", "08": "M", "09": "P", "10": "R", "11": "S", "12": "T"
        }
        giorno = self.data[:2]
        mese = self.data[3:5]
        anno = self.data[6:10]

        self.anno_codice = str(int(anno) % 100).zfill(2)  # Assicura due cifre
        self.giorno_codice = int(giorno) + 40 if self.sesso == "F" else giorno
        self.mese_codice = giorni_mesi[mese]



# gestione comune di nascita
class ComuneDiNascita:
    def __init__(self, comune):
        self.comune = comune.upper()
        self.codici_catastali = {
            "TORINO": "L219", "ROMA": "H501", "MILANO": "F205", "BRESCIA": "B157", "NAPOLI": "F839",
            "BARI": "A662", "VENEZIA": "I312", "GENOVA": "D627", "MARINO": "E958", "CATANZARO": "B547",
            "ANCONA": "A269", "FIRENZE": "D612", "PARIGI": "P001", "LONDRA": "L002", "NEW YORK": "NY01",
            "AVEZZANO" : "A515"
        }

    def get_codici_catastali(self):
        return self.codici_catastali[self.comune]


class CarattereDiControllo:
    def __init__(self,codice):
        self.codice = codice
    def calcola(self):
        valori_pari = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
            'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
        }

        valori_dispari = {
            '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
            'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
            'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
            'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z':23 }

        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        somma = 0

        for i, char in enumerate(self.codice):
            if i % 2 == 0:  # Indici dispari (posizioni 1,3,5...) nel codice (index 0-based)
                somma += valori_dispari[char]  # Default a 0 se il carattere non è nella mappa
            else:  # Indici pari (posizioni 2,4,6...)
                somma += valori_pari[char]

        resto = somma % 26
        return alfabeto[resto]


# funzione per generare il codice fiscale
def genera_codice_fiscale():
    cognome = input("Inserisci il cognome: ")
    nome = input("Inserisci il nome: ")
    data_nascita = input("Inserisci la data di nascita (GG/MM/AAAA): ")
    sesso = input("Inserisci il sesso (M/F): ")
    comune = input("Inserisci il comune di nascita: ")

    cognome_cod = StringaDiTesto(cognome).risStringa(tipo="cognome")
    nome_cod = StringaDiTesto(nome).risStringa(tipo="nome")
    data_nascita_obj = DataDiNascita(data_nascita, sesso)
    comune_cod = ComuneDiNascita(comune).get_codici_catastali()

    codice_base = f"{cognome_cod}{nome_cod}{data_nascita_obj.anno_codice}{data_nascita_obj.mese_codice}{str(data_nascita_obj.giorno_codice).zfill(2)}{comune_cod}"
    carattere_speciale = CarattereDiControllo(codice_base).calcola()
    codice_fiscale = codice_base + carattere_speciale


    print(f"Codice fiscale generato: {codice_fiscale}")

# Avvio della generazione del codice fiscale
genera_codice_fiscale()
