from pathlib import Path
from price_watch.fetcher import fetch_products_from_api, load_local_products
from price_watch.cli import parse_arguments
from price_watch.analyzer import Analyzer
from price_watch.exporter import PriceReport

def main():
    # 1. Récupération des arguments du CLI
    params = parse_arguments()
    
    chemin_fichier_json = Path("products_dump.json")
    
    # 2. Gestion du cache / API
    if params.fetch or not chemin_fichier_json.exists():
        print("🔄 Récupération des données fraîche depuis l'API Pokémon...")
        fetch_products_from_api(chemin_fichier_json=chemin_fichier_json)
    else:
        print("📂 Chargement des données depuis le cache local (products_dump.json)...")
    
    
    # 3. Chargement des objets métiers
    products = load_local_products(chemin_fichier_json)
    
    if not products:
        print("⚠️ Aucune donnée de produit disponible pour l'analyse. Vérifiez l'API ou le fichier JSON.")
        return

    # 4. Analyse statistique
    analyzer = Analyzer(products)
    
    global_stats = {
        "total": len(products),
        "mean": analyzer.calculate_mean(),
        "stdev": analyzer.calculate_stdev()
    }

    anomalies_detectees = analyzer.find_anomalies(threshold_factor=params.threshold)
    
    # 5. Génération et export des rapports
    exporter = PriceReport(
        global_stats=global_stats, 
        anomalies=anomalies_detectees, 
        output_dir=Path(params.output)
    )
    
    exporter.save_txt_report()
    exporter.save_json_report()
    
    print(f"🚀 Fin de l'exécution. Rapports disponibles dans le dossier : '{params.output}/'")

if __name__ == "__main__":
    main()