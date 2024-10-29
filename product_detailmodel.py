import sqlite3

def init_db():
    """Initialize the database and create tables if they do not exist."""
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS wishlist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS exchange_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS cart (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT)''')
    conn.commit()
    conn.close()

def add_like(product_name):
    """Add a product to the wishlist."""
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("INSERT INTO wishlist (product_name) VALUES (?)", (product_name,))
    conn.commit()
    conn.close()
    print(f"Product '{product_name}' has been liked and added to wishlist.")

def add_exchange(product_name):
    """Initiate an exchange request for a product."""
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("INSERT INTO exchange_requests (product_name) VALUES (?)", (product_name,))
    conn.commit()
    conn.close()
    print(f"Exchange initiated for product '{product_name}'.")

def add_to_cart(product_name):
    """Add a product to the shopping cart."""
    conn = sqlite3.connect('localbarter.db')
    c = conn.cursor()
    c.execute("INSERT INTO cart (product_name) VALUES (?)", (product_name,))
    conn.commit()
    conn.close()
    print(f"Product '{product_name}' has been added to the cart.")

# Initialize the database when the module is imported
init_db()
