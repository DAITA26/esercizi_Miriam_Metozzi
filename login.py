class UsernameAlreadyExists(Exception):
    pass

class InvalidCredentials(Exception):
    pass

def users_registrati(file_path):
    #carico gli utenti dal file
    users = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        print(f"Il file '{file_path}' non esiste. Sarà creato automaticamente.")
    return users

def salvataggio_users(file_path, username, password):
    #salvo l'utente sul file
    with open(file_path, "a") as file:
        file.write(f"{username}:{password}\n")

def aggiorna_file(file_path, users):
    #sovrascrive il file con gli utenti aggiornati
    with open(file_path, "w") as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")

def user_salvati(file_path, users, username, password):
    #creo un nuovo account
    if username in users:
        raise UsernameAlreadyExists("Username già esistente. Provare uno differente.")
    users[username] = password  # Aggiorno il dizionario
    salvataggio_users(file_path, username, password)  # Salvo nel file
    print("Account creato con successo.")

def login(users, username, password):
    #effettuo il login
    if username not in users or users[username] != password:
        raise InvalidCredentials("Username o password non validi.")
    print("Accesso consentito.")
    return True
def modifica_password(file_path, users, username):
    #modifica la password dell'utente
    nuova_password = input("Inserisci la nuova password: ")
    users[username] = nuova_password  # Aggiorna il dizionario
    aggiorna_file(file_path, users)  # Sovrascrive il file con la nuova password
    print("Password modificata con successo.")

def main():
    file_path = "users.txt"
    users = users_registrati(file_path)

    print("Salve, per usufruire del servizio per favore si identifichi:")
    print("1. Premi 1 per registrarsi")
    print("2. Premi 2 se è già registrato")
    print("3 Premi 3 per modificare la password")

    choice = input("Scelga un'opzione: ")

    if choice == '1':
        username = input("Inserisca username: ")
        password = input("Inserisca password: ")
        try:
            user_salvati(file_path, users, username, password)  # Chiamata alla funzione per creare un account
        except UsernameAlreadyExists as e:
            print(e)
    elif choice == '2':
        username = input("Inserisca username: ")
        password = input("Inserisca password: ")
        try:
            login(users, username, password)  # Chiamata alla funzione per effettuare il login
        except InvalidCredentials as e:
            print(e)
    elif choice=='3':
        username = input("Inserisca username: ")
        password = input("Inserisca password: ")
        try:
            login(users, username, password) #verifica login
            modifica_password(file_path, users, username)
        except InvalidCredentials as e:
            print(e)
    else:
        print("Scelta non valida. Per favore riprova.")

if __name__ == "__main__":
    main()
