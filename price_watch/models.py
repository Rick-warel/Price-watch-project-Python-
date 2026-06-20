class Product:
    def __init__(self, id : str, name : str, price : float , currency : str = "USD", source : str = ""):
        self.id = id
        self.name = name
        self.price = price
        self.currency = currency
        self.source = source