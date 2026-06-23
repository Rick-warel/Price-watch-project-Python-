import requests
import json
from price_watch.models import Product



def fetch_products_from_api(chemin_fichier_json):
    
    url = "https://api.pokemontcg.io/v2/cards?pageSize=10"
    # 1. Utilise requests pour récupérer les données
    response = requests.get(url)
    if response.status_code == 200:
        data_brute = response.json()
        chemin_cache = chemin_fichier_json
        with open(chemin_cache, "w", encoding="utf-8") as f:
            json.dump(data_brute, f, indent=4)
        print("💾 Données brutes sauvegardées avec succès dans products_dump.json !")
        
    else:
        print(f"❌ Erreur lors de la requête : {response.status_code}")
        
    # 2. Utilise json et Path pour sauvegarder la réponse dans un fichier 'products_dump.json'


def load_local_products(chemin_fichier_json):
    if chemin_fichier_json.exists():
        with open(chemin_fichier_json, "r", encoding="utf-8") as f:
            data_brute = json.load(f)
            products = []
            for item in data_brute.get("data", []):
                # Essaie d'abord tcgplayer, puis cardmarket, sinon 0.0
                price = item.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("market", None)
                if price is None:
                    price = item.get("cardmarket", {}).get("prices", {}).get("holofoil", {}).get("market", 0.0)
                
                product = Product(
                    id=item.get("id", ""),
                    name=item.get("name", ""),
                    price=float(price or 0.0),
                    currency="USD",
                    source="Pokémon TCG API"
                )
                products.append(product)
            return products
    else:
        print(f"❌ Le fichier {chemin_fichier_json} n'existe pas.")
        return []
    
    

