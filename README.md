# Education Madagascar - Scraper & API Baccalauréat

Ce projet contient un scraper pour le site EducMad et une API FastAPI pour rechercher les sujets et corrections du baccalauréat malgache.

## Nouveautés : Conversion HTML vers PDF

Certaines sessions anciennes (entre 2000 et 2012) sont stockées sur EducMad sous forme de pages HTML interactives plutôt que de fichiers PDF directs. Nous avons ajouté des outils pour gérer ce cas :

- **`convert_to_pdf.py`** : Script Python qui utilise `pdfkit` et `wkhtmltopdf` pour capturer le contenu principal de ces pages et générer des fichiers PDF formatés proprement.
- **`update_json.py`** : Script pour intégrer les nouveaux liens des PDF générés dans le fichier de données principal `bac_madagascar_data.json`.
- **Dossier `pdfs/`** : Répertoire contenant les fichiers PDF générés pour les sessions de Philosophie série A (1999-2011).

## Utilisation

Les données consolidées sont disponibles dans le fichier `bac_madagascar_data.json`, qui peut être utilisé par l'API ou d'autres applications front-end.
