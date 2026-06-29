import pytest
from price_watch.models import Product
from price_watch.analyzer import Analyzer


def test_calculate_mean_with_simple_values():
    # Arrange
    products = [
        Product(id="1", name="Carte A", price=10.0),
        Product(id="2", name="Carte B", price=20.0),
        Product(id="3", name="Carte C", price=30.0),
    ]
    analyzer = Analyzer(products)
    
    # Act
    result = analyzer.calculate_mean()
    
    # Assert
    assert result == 20.0


def test_init_filters_out_products_with_zero_or_negative_price():
    # Arrange : un produit valide, un produit à prix 0 (qui doit être filtré)
    products = [
        Product(id="1", name="Carte A", price=10.0),
        Product(id="2", name="Carte B", price=0.0),
    ]
    
    # Act
    analyzer = Analyzer(products)
    
    # Assert : seul le produit à 10.0 doit avoir survécu au filtre
    assert len(analyzer.list_produit_sup_0) == 1
    assert analyzer.list_produit_sup_0[0].id == "1"


def test_init_limits_products_when_limit_is_provided():
    products = [
        Product(id="1", name="Carte A", price=10.0),
        Product(id="2", name="Carte B", price=20.0),
        Product(id="3", name="Carte C", price=30.0),
    ]

    analyzer = Analyzer(products, limit=2)

    assert len(analyzer.list_produit_sup_0) == 2
    assert [product.id for product in analyzer.list_produit_sup_0] == ["1", "2"]


def test_calculate_stdev_with_not_enough_data():
    
    products = [
        Product(id="1", name="Carte A", price=10.0),
    ]
    
    analyzer = Analyzer(products)
    
    with pytest.raises(ValueError) as excinfo:
        analyzer.calculate_stdev()
        


def test_calculate_stdev_with_enough_data():
    products = [
        Product(id="1", name="Carte A", price=10.0),
        Product(id="2", name="Carte B", price=20.0),
    ]
    
    analyzer = Analyzer(products)
    
    result = analyzer.calculate_stdev()
    
    # L'écart type pour [10, 20] est 7.0710678118654755
    assert result == pytest.approx(7.0710678118654755, rel=1e-9)

