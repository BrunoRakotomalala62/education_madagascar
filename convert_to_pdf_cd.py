import os
import requests
from bs4 import BeautifulSoup
import pdfkit
import json

# Configuration
BASE_URL = "http://mediatheque.accesmad.org/educmad/mod/page/view.php?id="
SESSIONS_CD = {
    "2011": "6177",
    "2010": "6178",
    "2009": "6179",
    "2008": "6180",
    "2007": "6181",
    "2005": "6182",
    "2004": "6183",
    "2003": "6184",
    "2002": "6185",
    "2000": "6186",
    "1999": "6187"
}

OUTPUT_DIR = "/home/ubuntu/education_madagascar/pdfs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_session(year, page_id):
    url = f"{BASE_URL}{page_id}"
    print(f"Traitement de la session CD {year} (ID: {page_id})...")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
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
                </style>
            </head>
            <body>
                {content.decode_contents()}
            </body>
            </html>
            """
            
            output_path = os.path.join(OUTPUT_DIR, f"Philosophie_SerieCD_{year}.pdf")
            pdfkit.from_string(html_content, output_path)
            print(f"PDF généré : {output_path}")
            return output_path
    except Exception as e:
        print(f"Erreur lors de la conversion de {year}: {e}")
    return None

if __name__ == "__main__":
    results = {}
    for year, page_id in SESSIONS_CD.items():
        pdf_path = convert_session(year, page_id)
        if pdf_path:
            results[year] = pdf_path
