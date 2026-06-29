from price_watch.models import Product
import pytest



def test_product_initialization_success():
    
    prod = Product(id = "1", name= "produit_test_1", price=20.00)
    
    assert prod.id == "1"
    assert prod.name == "produit_test_1"
    assert prod.price == 20.00
    assert prod.currency == "USD"
    assert prod.source == ""

def test_product_initialization_empty_id_raises_error():
    
    with pytest.raises(ValueError, match="ID cannot be empty"):
        Product(id="", name="Cafetière", price=49.99)

def test_product_initialization_empty_name_raises_error():        
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product(id="4", name="", price=49.99)

def test_product_initialization_empty_price_raises_error():        
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product(id="4", name="product2", price= -2)