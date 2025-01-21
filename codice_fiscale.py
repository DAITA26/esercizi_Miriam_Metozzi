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
        self.mesi_lettere = {
            "01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "H",
            "07": "L", "08": "M", "09": "P", "10": "R", "11": "S", "12": "T"
        }
    def calcola_codice(self):
        giorno = int(self.data[:2])
        mese = self.data[3:5]
        anno = self.data[6:10]
        anno_codice = str(int(anno) % 100).zfill(2)
        giorno_codice = giorno + 40 if self.sesso == "F" else giorno
        return anno_codice, self.mesi_lettere[mese], str(giorno_codice).zfill(2)


# gestione comune di nascita
class ComuneDiNascita:
    def __init__(self, comune, file_codici="codici_catastali.txt"):
        self.comune = comune.upper()
        self.file_codici = file_codici
        self.codici_catastali = self.leggi_codici_catastali()

    def leggi_codici_catastali(self):
        codici = {}
        try:
            with open(self.file_codici, "r", encoding="utf-8") as file:
                for linea in file:
                    parti = linea.strip().split(";")
                    if len(parti) == 2:
                        comune, codice = parti
                        codici[comune.upper()] = codice
        except FileNotFoundError:
            print(f"Errore: Il file {self.file_codici} non è stato trovato.")
        return codici

    def codice_catastale(self):
        return self.codici_catastali.get(self.comune, "XXXX")


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
class CodiceFiscale:
    def __init__(self, nome, cognome, data_nascita, comune, sesso):
        self.nome = StringaDiTesto(nome)
        self.cognome = StringaDiTesto(cognome)
        self.data_nascita = DataDiNascita(data_nascita, sesso)
        self.comune = ComuneDiNascita(comune)

    def genera_codice_fiscale(self):
        anno, mese, giorno = self.data_nascita.calcola_codice()
        codice_base = (
            self.cognome.risStringa(tipo="cognome") +
            self.nome.risStringa(tipo="nome") +
            anno + mese + giorno + self.comune.codice_catastale()
        )
        carattere_controllo = CarattereDiControllo(codice_base).calcola()
        return codice_base + carattere_controllo


if __name__ == "__main__":
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci la data di nascita (DD/MM/YYYY): ")
    comune = input("Inserisci il comune di nascita: ")
    sesso = input("Inserisci il sesso (M/F): ")

    codice_fiscale = CodiceFiscale(nome, cognome, data_nascita, comune, sesso)
    print("Il codice fiscale generato è:", codice_fiscale.genera_codice_fiscale())