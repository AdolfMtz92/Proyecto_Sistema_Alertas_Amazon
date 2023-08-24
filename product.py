class Product:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.current_price = 0  # Precio actualizado desde Amazon

    def update_price(self, new_price):
        self.current_price = new_price

