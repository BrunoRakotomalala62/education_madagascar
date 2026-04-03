import requests
from bs4 import BeautifulSoup
import json
import re
import time

BASE_URL = "http://mediatheque.accesmad.org/educmad/course/view.php?id="

def get_pdf_links(course_id, course_name):
    url = f"{BASE_URL}{course_id}"
    print(f"Scraping {course_name} (ID: {course_id})...")
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    
    # Moodle structure: activities are usually in 'activityinstance' or 'instancename'
    # We look for all links and filter those that look like PDF resources
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True)
        
        # Check if it's a resource link (pluginfile.php or mod/resource)
        if 'pluginfile.php' in href or 'mod/resource' in href:
            # Extract year
            year_match = re.search(r'(20\d{2}|19\d{2})', text)
            year = year_match.group(1) if year_match else "Inconnu"
            
            # Determine type (sujet/énoncé vs correction/corrigé)
            type_val = "sujet"
            if any(word in text.lower() for word in ["corrigé", "correction", "corrigé"]):
                type_val = "correction"
            
            # Determine serie from text or course name
            serie = "Inconnue"
            for s in ["série A", "série C", "série D", "série L", "série S", "OSE"]:
                if s.lower() in text.lower() or s.lower() in course_name.lower():
                    serie = s.replace("série ", "")
                    break
            
            # Clean title
            title = text.replace("Sélectionner l’activité", "").strip()
            if not title:
                title = f"{course_name} {year}"

            links.append({
                "titre": title,
                "session": year,
                "url_pdf": href,
                "matiere": course_name,
                "serie": serie,
                "type": type_val
            })
            
    return links

def main():
    with open('course_structure.json', 'r') as f:
        structure = json.load(f)
    
    all_data = []
    
    # Process Annales bacc A - C - D
    abcd = structure["Annales bacc A - C - D"]
    for subcat_name, subcat_data in abcd["subcategories"].items():
        for course_name, course_id in subcat_data["courses"].items():
            all_data.extend(get_pdf_links(course_id, course_name))
            time.sleep(1) # Be nice to the server
            
    # Process Annales bacc L - S - OSE
    lso = structure["Annales bacc L - S - OSE"]
    for course_name, course_id in lso["courses"].items():
        all_data.extend(get_pdf_links(course_id, course_name))
        time.sleep(1)

    with open('bac_madagascar_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"Scraping finished. Total items: {len(all_data)}")

if __name__ == "__main__":
    main()
