Script Python qui récupère des prix depuis une API publique (ex: Open Food Facts, Pokémon TCG API), les stocke en JSON, détecte les anomalies (prix en dehors de la moyenne ± 2σ) et génère un rapport texte. Très proche d'un outil de veille tarifaire en entreprise.

- cli.py permet de définir les différentes possibilités en ligne de commande. une façon d'avoir des résultats différents en changeant par exemple la source des données, le nom des fichiers de rapport et d'export, ou le seuil d'anomalie, sans avoir à modifier le code.

- le point d'entrée de notre script est le fichier main.py
  la mission de notre main.py est d'orchestrer le passage des données entre les différentes fonctionnalités du script qu'il importe au préalable. il commence par vérifier les paramètres passés en ligne de commande. si il y a des arguments il adapte l'exécution du script, sinon il utilise les données du cache et travaille avec. la récupération des données est liée au fichier fetcher.py. une fois les données récupérées, il les analyse avec le fichier analyzer.py à qui il passe en paramètre les données récupérées. une fois l'analyse terminée, le résultat de l'analyse est stocké dans un dictionnaire (global_stats) et les anomalies sont stockées dans une variable (anomalies_detectees). l'étape suivante est la génération du rapport.txt et l'export en fichier json

      liste des commandes possibles

      1. Lancement classique (Mode par défaut) Si tu veux utiliser les données déjà téléchargées dans ton fichier JSON local, appliquer le seuil de 2.0 et enregistrer dans le dossier par défaut :
      Bash
      python main.py

      2. Forcer la mise à jour des données (API)
      Si tu veux vider le cache et forcer le script à aller chercher les prix tout frais du jour sur l'API Pokémon avant de faire l'analyse :
      Bash
      python main.py --fetch

      3. Ajuster la sensibilité du détecteur d'anomalies
      Si le marketing te demande d'être plus strict (par exemple, resserrer la barrière à 1.5 fois l'écart-type au lieu de 2.0) :
      Bash
      python main.py --threshold 1.5

      4. Changer le dossier de sortie des rapports
      Si tu veux que les rapports textuels et JSON soient rangés dans un dossier spécifique (qui sera créé automatiquement s'il n'existe pas) :
      Bash
      python main.py --output mes_rapports_juin

      Le combo total
      Tu peux bien sûr combiner toutes les options en une seule ligne si tu veux tout personnaliser d'un coup :
      Bash
      python main.py --fetch --threshold 1.8 --output monitoring_api

- fetcher.py est le fichier chargé de récupérer les données depuis l'API et de les stocker en local dans un fichier json qui servira de cache au cas où un souci surviendrait avec l'API par exemple. il n'a besoin que du chemin du fichier json où stocker les données.
  fetch_products_from_api : récupère les données et les stocke

  load_local_products : récupère uniquement les données dont on a besoin, met chaque produit en forme à l'aide du modèle model.py et renvoie tous les produits sous forme d'une liste.

- analyzer.py est chargé d'analyser les données et de nous ressortir 3 éléments. il a besoin de la liste des produits comme paramètre
  calculate_mean : calcule la moyenne et renvoie un float
  calculate_stdev : calcule l'écart-type et renvoie un float
  find_anomalies : détecte toutes les anomalies et renvoie une liste

- exporter.py est chargé de générer le rapport.txt et l'export des résultats de l'analyse en json. il a besoin de notre dictionnaire et de la liste des anomalies issus de analyzer
  save_txt_report : écrit le rapport.txt
  save_json_report : exporte les données en json
