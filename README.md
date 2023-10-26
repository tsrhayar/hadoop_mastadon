# Scraping and Data Processing with Python

Ce projet comprend des scripts Python pour scraper des données à partir de Mastodon, les traiter, et les stocker dans HBase.

## Utilisation

### Prérequis

Assurez-vous d'installer les bibliothèques suivantes avant d'exécuter les scripts :

- requests
- json
- pandas
- hdfs
- BeautifulSoup

### Exemple d'utilisation

Voici comment vous pouvez utiliser ces scripts :

1. Exécutez `scrapping.py` pour scraper les données de Mastodon et les stocker dans HDFS.
2. Exécutez `mapper.py` pour traiter les données.
3. Exécutez `hbase.py` pour stocker les données dans HBase.

## Auteurs

- Votre nom

## Licence

Ce projet est sous licence MIT.

## Contributions

Les contributions sont les bienvenues. N'hésitez pas à ouvrir une demande de tirage.

# Scraping, Processing, and Storing Data with Python

## Description

Ce projet est une collection de scripts Python qui permettent de collecter des données à partir de Mastodon, de les traiter et de les stocker dans HBase. Le projet est divisé en trois scripts principaux : `scrapping.py`, `mapper.py`, et `hbase.py`.

## Fonctionnalités

- `scrapping.py`: Ce script utilise la bibliothèque `requests` pour extraire des données à partir de Mastodon, nettoie et formate ces données, puis les stocke dans un système de fichiers distribué HDFS.

- `mapper.py`: Ce script prend les données extraites par `scrapping.py`, effectue une analyse et un mappage des informations pertinentes, et génère une sortie structurée pour le stockage.

- `hbase.py`: Ce script connecte le projet à une base de données NoSQL HBase et stocke les données mappées dans des tables spécifiques.

## Prérequis

Avant d'exécuter ces scripts, assurez-vous d'installer les dépendances suivantes :

- `requests`
- `json`
- `pandas`
- `hdfs`
- `BeautifulSoup`

Vous pouvez les installer à l'aide de `pip` :

```bash
pip install requests json pandas hdfs beautifulsoup4

## Exemple d'utilisation
Un exemple d'utilisation complet est fourni dans le script scrapping.py qui extrait des données de Mastodon. Vous pouvez le personnaliser pour votre propre utilisation.

```python
if __name__ == "__main__":
    URL = 'https://mastodon.social/api/v1/timelines/public'
    params = {
        'limit': 40,
    }
    since = pd.Timestamp(year=2021, month=5, day=1, tz='utc')
    
    hdfs_url = 'http://localhost:9870'
    hdfs_filename = 'mastodon_data'

    toots_data = scrape_mastodon_timeline(URL, params, since, hdfs_url, hdfs_filename)