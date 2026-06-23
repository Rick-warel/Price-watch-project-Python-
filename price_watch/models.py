class Product:
    def __init__(self, id : str, name : str, price : float , currency : str = "USD", source : str = ""):
        
        if id != "":
            self.id = id
        else:
            raise ValueError("ID cannot be empty")
        
        if name != "":
            self.name = name
        else:
            raise ValueError("Name cannot be empty")
        
        if price >= 0:
            self.price = price
        else:
            raise ValueError("Price cannot be empty or negative")
        
        self.currency = currency
        self.source = source 


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "currency": self.currency,
            "source": self.source
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            price=data.get("price", 0.0),
            currency=data.get("currency", "USD"),
            source=data.get("source", "")
        )
        
    def __str__(self):
        """Affichage propre et lisible pour les humains"""
        return f"📦 {self.name} - {self.price} {self.currency} (Source: {self.source if self.source else 'Inconnue'})"

    def __repr__(self):
        """Affichage technique idéal pour le débogage dans les listes"""
        return f"Product(id='{self.id}', name='{self.name}', price={self.price}, currency='{self.currency}', source='{self.source}')"

