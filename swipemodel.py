import sqlite3

# Sample items
items = [
    {
        "name": "Firefox X23 Hybrid",
        "offered_by": "Tara",
        "distance": "1.7km away",
        "image_url": "https://images.pexels.com/photos/4542852/pexels-photo-4542852.jpeg"
    },
    {
        "name": "Mountain Pro",
        "offered_by": "Jake",
        "distance": "2.5km away",
        "image_url": "https://images.pexels.com/photos/946451/pexels-photo-946451.jpeg"  # Updated URL with valid image
    },
    {
        "name": "City Cruiser",
        "offered_by": "Mia",
        "distance": "3.2km away",
        "image_url": "https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg"
    }
]

current_item_index = 0

def get_next_item():
    global current_item_index
    item = items[current_item_index]
    current_item_index = (current_item_index + 1) % len(items)  # Cycle through items
    return item

def add_to_wishlist(item):
    conn = sqlite3.connect('wishlist.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS wishlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            offered_by TEXT,
            distance TEXT,
            image_url TEXT
        )
    ''')
    c.execute('''
        INSERT INTO wishlist (name, offered_by, distance, image_url)
        VALUES (?, ?, ?, ?)
    ''', (item['name'], item['offered_by'], item['distance'], item['image_url']))
    conn.commit()
    conn.close()
