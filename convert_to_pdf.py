import os
import requests
from bs4 import BeautifulSoup
import pdfkit
import json

# Configuration
BASE_URL = "http://mediatheque.accesmad.org/educmad/mod/page/view.php?id="
SESSIONS_A = {
    "2011": "6164",
    "2010": "6163",
    "2009": "6162",
    "2008": "6161",
    "2007": "6160",
    "2005": "6159",
    "2004": "6158",
    "2003": "6157",
    "2002": "6156",
    "2001": "6155",
    "2000": "6154",
    "1999": "6153"
}

OUTPUT_DIR = "/home/ubuntu/education_madagascar/pdfs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_session(year, page_id):
    url = f"{BASE_URL}{page_id}"
    print(f"Traitement de la session {year} (ID: {page_id})...")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraire le contenu principal
        content = soup.find('div', {'role': 'main'})
        if not content:
            content = soup.find('div', {'id': 'region-main'})
            
        if content:
            html_content = f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }}
                    h1, h2 {{ color: #2c3e50; text-align: center; }}
                    .subject {{ margin-bottom: 20px; padding: 15px; border-bottom: 1px solid #eee; }}
                    .nb {{ font-weight: bold; color: #e74c3c; }}
                </style>
            </head>
            <body>
                {content.decode_contents()}
            </body>
            </html>
            """
            
            output_path = os.path.join(OUTPUT_DIR, f"Philosophie_SerieA_{year}.pdf")
            pdfkit.from_string(html_content, output_path)
            print(f"PDF généré : {output_path}")
            return output_path
        else:
            print(f"Erreur : Contenu non trouvé pour {year}")
    except Exception as e:
        print(f"Erreur lors de la conversion de {year}: {e}")
    return None

if __name__ == "__main__":
    results = {}
    for year, page_id in SESSIONS_A.items():
        pdf_path = convert_session(year, page_id)
        if pdf_path:
            results[year] = pdf_path
            
    print("\nRésumé des conversions :")
    for year, path in results.items():
        print(f"{year}: {path}")
