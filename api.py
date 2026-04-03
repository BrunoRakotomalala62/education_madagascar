from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import json
from typing import List, Optional

app = FastAPI(title="Bac Madagascar API")

# Load data
try:
    with open("bac_madagascar_data.json", "r", encoding="utf-8") as f:
        bac_data = json.load(f)
except FileNotFoundError:
    bac_data = []

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Bac Madagascar</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100 p-8">
        <div class="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-md">
            <h1 class="text-3xl font-bold mb-6 text-gray-800">API Bac Madagascar - Documentation</h1>
            
            <p class="mb-4 text-gray-700">Bienvenue sur l'API Bac Madagascar. Cette API vous permet de rechercher des sujets et corrections du baccalauréat malgache par matière, série, type et session.</p>
            
            <h2 class="text-2xl font-semibold mb-4 text-gray-800">Endpoint de recherche: <code class="bg-gray-200 p-1 rounded">/recherche</code></h2>
            <p class="mb-4 text-gray-700">Utilisez cet endpoint pour filtrer les documents PDF. Tous les paramètres sont optionnels et peuvent être combinés.</p>
            
            <h3 class="text-xl font-medium mb-3 text-gray-800">Paramètres disponibles:</h3>
            <ul class="list-disc list-inside mb-6 ml-4 text-gray-700">
                <li><code class="bg-gray-200 p-1 rounded">matiere</code>: Nom de la matière (ex: <code class="bg-gray-200 p-1 rounded">philosophie</code>, <code class="bg-gray-200 p-1 rounded">mathématiques</code>, <code class="bg-gray-200 p-1 rounded">anglais</code>)</li>
                <li><code class="bg-gray-200 p-1 rounded">serie</code>: Série du baccalauréat (ex: <code class="bg-gray-200 p-1 rounded">A</code>, <code class="bg-gray-200 p-1 rounded">C</code>, <code class="bg-gray-200 p-1 rounded">D</code>, <code class="bg-gray-200 p-1 rounded">OSE</code>, <code class="bg-gray-200 p-1 rounded">L</code>, <code class="bg-gray-200 p-1 rounded">S</code>)</li>
                <li><code class="bg-gray-200 p-1 rounded">type</code>: Type de document (<code class="bg-gray-200 p-1 rounded">sujet</code> ou <code class="bg-gray-200 p-1 rounded">correction</code>)</li>
                <li><code class="bg-gray-200 p-1 rounded">session</code>: Année de la session (ex: <code class="bg-gray-200 p-1 rounded">2003</code>, <code class="bg-gray-200 p-1 rounded">2020</code>)</li>
            </ul>
            
            <h3 class="text-xl font-medium mb-3 text-gray-800">Exemples d'utilisation:</h3>
            <ul class="list-disc list-inside mb-6 ml-4 text-gray-700">
                <li><p>Tous les sujets de philosophie de la série A:</p><a href="/recherche?matiere=philosophie&serie=A&type=sujet" class="text-blue-500 hover:underline"><code>/recherche?matiere=philosophie&serie=A&type=sujet</code></a></li>
                <li><p>Toutes les corrections de mathématiques:</p><a href="/recherche?matiere=mathématiques&type=correction" class="text-blue-500 hover:underline"><code>/recherche?matiere=mathématiques&type=correction</code></a></li>
                <li><p>Sujets de physique de la série D pour la session 2015:</p><a href="/recherche?matiere=physique&serie=D&type=sujet&session=2015" class="text-blue-500 hover:underline"><code>/recherche?matiere=physique&serie=D&type=sujet&session=2015</code></a></li>
                <li><p>Toutes les corrections de la session 2020:</p><a href="/recherche?type=correction&session=2020" class="text-blue-500 hover:underline"><code>/recherche?type=correction&session=2020</code></a></li>
                <li><p>Tous les documents disponibles (sans filtre):</p><a href="/recherche" class="text-blue-500 hover:underline"><code>/recherche</code></a></li>
            </ul>
            
            <h2 class="text-2xl font-semibold mb-4 text-gray-800">Format de sortie:</h2>
            <p class="mb-4 text-gray-700">Les résultats sont retournés au format JSON, avec chaque élément contenant les clés suivantes:</p>
            <ul class="list-disc list-inside mb-6 ml-4 text-gray-700">
                <li><code class="bg-gray-200 p-1 rounded">titre</code>: Le titre du document (ex: "Philosophie A 2000")</li>
                <li><code class="bg-gray-200 p-1 rounded">session</code>: L'année de la session (ex: "2000")</li>
                <li><code class="bg-gray-200 p-1 rounded">url_pdf</code>: L'URL directe pour télécharger le fichier PDF</li>
            </ul>
            
            <h2 class="text-2xl font-semibold mb-4 text-gray-800">Dépôt GitHub:</h2>
            <p class="mb-4 text-gray-700">Le code source de cette API et du scraper est disponible sur GitHub:</p>
            <a href="https://github.com/BrunoRakotomalala62/education_madagascar" class="text-blue-500 hover:underline">https://github.com/BrunoRakotomalala62/education_madagascar</a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/recherche")
def recherche(
    matiere: Optional[str] = Query(None, description="Matière (ex: philosophie, mathématiques)"),
    serie: Optional[str] = Query(None, description="Série (ex: A, C, D, OSE, L, S)"),
    type: Optional[str] = Query(None, description="Type (sujet ou correction)"),
    session: Optional[str] = Query(None, description="Année de la session (ex: 2003)")
):
    results = []
    for item in bac_data:
        match = True
        if matiere and matiere.lower() not in item["matiere"].lower():
            match = False
        if serie and serie.lower() not in item["serie"].lower():
            match = False
        if type and type.lower() != item["type"].lower():
            match = False
        if session and session != item["session"]:
            match = False
        
        if match:
            results.append({
                "titre": item["titre"],
                "session": item["session"],
                "url_pdf": item["url_pdf"]
            })
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
