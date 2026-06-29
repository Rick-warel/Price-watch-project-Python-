import statistics

class Analyzer:
    def __init__(self, products, limit=None):
        filtered_products = [p for p in products if p.price > 0]
        if limit is not None:
            filtered_products = filtered_products[:limit]
        self.list_produit_sup_0 = filtered_products

    def calculate_mean(self):
        moyenne = statistics.mean([product.price for product in self.list_produit_sup_0])
        return moyenne

    def calculate_stdev(self):
        if len(self.list_produit_sup_0) < 2:
            raise ValueError("Pas assez de produits pour calculer l'écart type (au moins 2 requis).")
        return statistics.stdev([p.price for p in self.list_produit_sup_0])
    
    def find_anomalies(self,threshold_factor: float = 2.0):
        moyenne = self.calculate_mean()
        ecart_type = self.calculate_stdev()
        list_produit_anomali = []
        for product in self.list_produit_sup_0:
            if product.price > (moyenne + (ecart_type * threshold_factor)) or product.price < (moyenne - (ecart_type * threshold_factor)):
                list_produit_anomali.append(product)
        return list_produit_anomali
