
import requests
import json
from price_watch.models import Product


def fetch_products_from_api(chemin_fichier_json, url="https://api.pokemontcg.io/v2/cards?pageSize=60"):
    response = requests.get(url)
    response.raise_for_status()  # lève une exception si status != 200, plus propre que if/else
    
    data_brute = response.json()
    with open(chemin_fichier_json, "w", encoding="utf-8") as f:
        json.dump(data_brute, f, indent=4)
    
    return data_brute


def load_local_products(chemin_fichier_json):
    if not chemin_fichier_json.exists():
        raise FileNotFoundError(f"Le fichier {chemin_fichier_json} n'existe pas.")
    
    with open(chemin_fichier_json, "r", encoding="utf-8") as f:
        data_brute = json.load(f)
    
    products = []
    for item in data_brute.get("data", []):
        price = item.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("market")
        if price is None:
            price = item.get("cardmarket", {}).get("prices", {}).get("holofoil", {}).get("market", 0.0)
        
        products.append(Product(
            id=item.get("id", ""),
            name=item.get("name", ""),
            price=float(price or 0.0),
            currency="USD",
            source="Pokémon TCG API"
        ))
    return products

