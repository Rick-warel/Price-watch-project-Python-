from pathlib import Path
from price_watch.fetcher import fetch_products_from_api
from price_watch.fetcher import load_local_products
from price_watch.analyzer import Analyzer



def main():
    chemin_fichier_json = Path("products_dump.json")
    appel_api = fetch_products_from_api(chemin_fichier_json)
    products = load_local_products(chemin_fichier_json)

    analyzer = Analyzer(products)
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