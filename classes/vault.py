"""
A vault for storing username/password pairs including the service they belong to.
Using sqlite to store the data
"""

import sqlite3


class Vault:
    def __init__(self):
        self.conn = sqlite3.connect("./databases/vault.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS vault (
                service TEXT,
                username TEXT,
                password TEXT
            )
            """
        )
        self.conn.commit()

    def add_entry(self, service, username, password):
        self.cursor.execute(
            """
            INSERT INTO vault (service, username, password)
            VALUES (?, ?, ?)
            """,
            (service, username, password),
        )
        self.conn.commit()

    def get_entry(self, service):
        self.cursor.execute(
            """
            SELECT username, password FROM vault WHERE service = ?
            """,
            (service,),
        )
        return self.cursor.fetchone()

    def get_all_entries(self):
        self.cursor.execute(
            """
            SELECT service, username, password FROM vault
            """
        )


"""
Generate some test cases for each function
"""
# vault = Vault()
# vault.add_entry("gmail", "testuser", "testpassword")
# print(vault.get_entry("gmail"))
# print(vault.get_all_entries())
# vault.conn.close()
