class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Product:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

class Exchange:
    def __init__(self, user_product, exchanged_product, exchange_partner):
        self.user_product = user_product
        self.exchanged_product = exchanged_product
        self.exchange_partner = exchange_partner
