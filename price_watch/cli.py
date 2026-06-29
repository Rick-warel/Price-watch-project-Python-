import argparse

def parse_arguments():
    """
    Configure et analyse les arguments de la ligne de commande.
    :return: Un objet contenant les arguments capturés (args.threshold, args.fetch, args.output)
    """
    # 1. Création du parser avec une description claire de l'outil
    parser = argparse.ArgumentParser(
        description="🛡️ Price Watch - Détecteur d'anomalies de prix pour cartes Pokémon"
    )
    
    # 2. Option pour régler la sensibilité statistique (le fameux facteur multiplicateur)
    parser.add_argument(
        "-t", "--threshold",
        type=float,
        default=2.0,
        help="Facteur multiplicateur de l'écart-type pour le seuil d'anomalie (Défaut : 2.0)"
    )
    
    # 3. Option pour forcer le téléchargement depuis l'API (Drapeau/Flag True ou False)
    parser.add_argument(
        "-f", "--fetch",
        action="store_true",
        help="Force la récupération de nouvelles données depuis l'API Pokémon et met à jour le cache"
    )
    
    # 4. Option pour personnaliser le dossier de sortie des rapports
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="output_reports",
        help="Nom du dossier où seront sauvegardés les rapports (Défaut : output_reports)"
    )
    
    return parser.parse_args()