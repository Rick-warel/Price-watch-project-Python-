from pathlib import Path
import json
from price_watch.models import Product

class PriceReport:
    def __init__(self, global_stats: dict, anomalies: list[Product], output_dir: Path):
        self.global_stats = global_stats
        self.anomalies = anomalies
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    
    def save_txt_report(self, filename: str = "rapport_prix.txt"):
        chemin_fichier_txt = self.output_dir / filename
        with open(chemin_fichier_txt, "w", encoding="utf-8") as f:
            f.write("==================================================\n")
            f.write("       RAPPORT AUTOMATIQUE DE VEILLE TARIFAIRE     \n")
            f.write("==================================================\n\n")
            f.write("📊 STATISTIQUES GLOBALES DU MARCHÉ :\n")
            f.write(f"----------------------------------\n")
            f.write(f"\nLe nombre total de cartes analysées : {self.global_stats.get("total")} \n" )
            f.write(f"\nLa moyenne globale des prix : {self.global_stats.get("mean")} \n" )
            f.write(f"\nL'écart-type : {self.global_stats.get("stdev")} \n" )
            if not self.anomalies:
                f.write("✅ Aucune anomalie détectée sur ce sprint. Les prix sont stables.\n")
            else:
                f.write(f"⚠️ {len(self.anomalies)} produit(s) suspect(s) identifié(s) :\n\n")
                for index, product in enumerate(self.anomalies, 1):
                    # 🌟 C'est ici que ta méthode magique __str__ de Product s'appelle automatiquement !
                    f.write(f" {index}. {product}\n")
            f.write("\n==================================================\n")
            f.write("Fin du rapport d'analyse.\n")
        
    
    
    def save_json_report(self, filename: str = "anomalies.json"):
        """Exporte la liste des anomalies au format JSON pour être lue par d'autres applications"""
        chemin_fichier = self.output_dir / filename
        
        # 🔄 Transmission : On transforme nos objets complexes en dictionnaires bruts
        anomalies_serialisees = [product.to_dict() for product in self.anomalies]
        
        # Structure propre du JSON final
        export_data = {
            "metadata": {
                "total_analyzed": self.global_stats.get("total", 0),
                "market_mean": self.global_stats.get("mean", 0.0),
                "market_stdev": self.global_stats.get("stdev", 0.0),
                "anomalies_count": len(self.anomalies)
            },
            "anomalies": anomalies_serialisees
        }
        
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=4, ensure_ascii=False)
            print(f"💾 Rapport JSON exporté avec succès : {chemin_fichier}")
