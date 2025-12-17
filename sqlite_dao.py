# sqlite_dao.py
import sqlite3
from etape1 import Produit, Client

class SQLiteDAO:
    def __init__(self, db_name="boutique.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS produit (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom TEXT,
                                prix REAL)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS client (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom TEXT,
                                email TEXT)""")
        self.conn.commit()

    def ajouter_produit(self, produit: Produit):
        self.cursor.execute("INSERT INTO produit (nom, prix) VALUES (?, ?)", (produit.nom, produit.prix))
        self.conn.commit()

    def lister_produits(self):
        self.cursor.execute("SELECT * FROM produit")
        return [Produit(*row) for row in self.cursor.fetchall()]

    def ajouter_client(self, client: Client):
        self.cursor.execute("INSERT INTO client (nom, email) VALUES (?, ?)", (client.nom, client.email))
        self.conn.commit()

    def lister_clients(self):
        self.cursor.execute("SELECT * FROM client")
        return [Client(*row) for row in self.cursor.fetchall()]

    def rechercher_client_email(self, email):
        self.cursor.execute("SELECT * FROM client WHERE email=?", (email,))
        row = self.cursor.fetchone()
        return Client(*row) if row else None

    def modifier_prix_produit(self, id, nouveau_prix):
        self.cursor.execute("UPDATE produit SET prix=? WHERE id=?", (nouveau_prix, id))
        self.conn.commit()
