# main.py
from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO
from etape1 import Produit, Client

def menu(dao):
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter produit")
        print("2. Lister produits")
        print("3. Ajouter client")
        print("4. Lister clients")
        print("5. Rechercher client par email")
        print("6. Modifier prix produit")
        print("0. Quitter")

        choix = input("Votre choix: ")

        if choix == "1":
            nom = input("Nom du produit: ")
            prix = float(input("Prix: "))
            dao.ajouter_produit(Produit(None, nom, prix))
        elif choix == "2":
            for p in dao.lister_produits():
                print(p)
        elif choix == "3":
            nom = input("Nom du client: ")
            email = input("Email: ")
            dao.ajouter_client(Client(None, nom, email))
        elif choix == "4":
            for c in dao.lister_clients():
                print(c)
        elif choix == "5":
            email = input("Email: ")
            client = dao.rechercher_client_email(email)
            print(client if client else "Client introuvable")
        elif choix == "6":
            id = int(input("ID du produit: "))
            prix = float(input("Nouveau prix: "))
            dao.modifier_prix_produit(id, prix)
        elif choix == "0":
            break

if __name__ == "__main__":
    choix_base = input("Choisir base (sqlite/mysql): ").lower()
    dao = SQLiteDAO() if choix_base == "sqlite" else MySQLDAO()
    menu(dao)
