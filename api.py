from fastapi import FastAPI, Query
import json
from typing import List, Optional

app = FastAPI(title="Bac Madagascar API")

# Load data
try:
    with open("bac_madagascar_data.json", "r", encoding="utf-8") as f:
        bac_data = json.load(f)
except FileNotFoundError:
    bac_data = []

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
    uvicorn.run(app, host="0.0.0.0", port=8000)
