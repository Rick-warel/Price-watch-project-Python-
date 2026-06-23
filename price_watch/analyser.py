from pathlib import Path
from price_watch.fetcher import fetch_products_from_api
from price_watch.fetcher import load_local_products
import statistics

chemin_fichier_json = Path("products_dump.json")

class Analizer:
    def __init__(self, products):
        self.products = products 
        self.list_produit_sup_0 = []
        for product in self.products:
            if product.price > 0:
                self.list_produit_sup_0.append(product)

    def calculate_mean(self):
        moyenne = statistics.mean([product.price for product in self.list_produit_sup_0])
        return moyenne

    def calculate_stdev(self):
        if len(self.list_produit_sup_0) > 2:
            stdev = statistics.stdev([product.price for product in self.list_produit_sup_0])
            return stdev 
        else:
            return "❌ Pas assez de produits pour calculer l'écart type (au moins 2 requis)."
    
    def find_anomalies(self, moyenne, ecat_type, threshold_factor: float = 2.0):
        list_produit_anomali = []
        for product in self.list_produit_sup_0:
            if product.price > (moyenne + (ecat_type * 2)) or product.price < (moyenne - (ecat_type * 2)):
                list_produit_anomali.append(product)
        return list_produit_anomali
    
def main():
    appel_api = fetch_products_from_api(chemin_fichier_json)
    products = load_local_products(chemin_fichier_json)

    analyzer = Analizer(products)
    mean_price = analyzer.calculate_mean()
    stdev_price = analyzer.calculate_stdev()
    list_anomalies = analyzer.find_anomalies(mean_price, stdev_price)
    
    print(mean_price)
    print(stdev_price)
    print("---------list des produits avec anomalie---------")
    for product in list_anomalies:
        print(product)
    
if __name__ == "__main__":
    main()

# for stdev in stdev_price:
#     print(stdev)