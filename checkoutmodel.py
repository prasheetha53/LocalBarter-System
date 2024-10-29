# checkoutmodel.py
import sqlite3

def init_db():
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    # Create tables if they don't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            value INTEGER,
            quantity INTEGER,
            location TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS contact_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            email TEXT,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_to_cart(product_name, value, quantity, location):
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("INSERT INTO cart (product_name, value, quantity, location) VALUES (?, ?, ?, ?)",
              (product_name, value, quantity, location))
    conn.commit()
    conn.close()

def update_quantity(product_id, quantity):
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("UPDATE cart SET quantity = ? WHERE id = ?", (quantity, product_id))
    conn.commit()
    conn.close()

def get_cart_items():
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cart")
    items = c.fetchall()
    conn.close()
    return items

def get_contact_details():
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact_details ORDER BY id DESC LIMIT 1")
    details = c.fetchone()
    conn.close()
    return details

def set_contact_details(phone, email, location):
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("INSERT INTO contact_details (phone, email, location) VALUES (?, ?, ?)", (phone, email, location))
    conn.commit()
    conn.close()

# Initialize the database
init_db()
