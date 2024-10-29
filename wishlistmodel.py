# wishlistmodel.py

import sqlite3

class WishlistModel:
    def __init__(self, db_name="wishlist.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create wishlist table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS wishlist (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                item_name TEXT NOT NULL,
                                image_url TEXT,
                                exchange_value INTEGER
                              )''')
        self.connection.commit()

    def add_to_wishlist(self, item_name, image_url, exchange_value):
        self.cursor.execute("INSERT INTO wishlist (item_name, image_url, exchange_value) VALUES (?, ?, ?)",
                            (item_name, image_url, exchange_value))
        self.connection.commit()

    def get_wishlist(self):
        self.cursor.execute("SELECT * FROM wishlist")
        return self.cursor.fetchall()

    def remove_from_wishlist(self, item_id):
        self.cursor.execute("DELETE FROM wishlist WHERE id=?", (item_id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
