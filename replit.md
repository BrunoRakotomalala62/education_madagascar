# Education Madagascar - Bac API

A FastAPI-based REST API for searching Madagascar baccalaureate (high school exam) subjects and corrections.

## Project Structure

- `api.py` — Main FastAPI application serving the API and HTML documentation
- `bac_madagascar_data.json` — Dataset of bac subjects and corrections (PDF links)
- `course_structure.json` — Course/subject structure data
- `scraper.py` — Scraper used to collect data from EducMad website

## Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **Server:** Uvicorn (dev), Gunicorn + UvicornWorker (prod)
- **Port:** 5000

## Running

The app starts automatically via the "Start application" workflow:
```
python api.py
```

## API Endpoints

- `GET /` — HTML documentation page
- `GET /recherche` — Search bac documents with optional query params:
  - `matiere` — Subject name (e.g., philosophie, mathématiques)
  - `serie` — Bac series (A, C, D, OSE, L, S)
  - `type` — Document type (sujet or correction)
  - `session` — Year (e.g., 2003, 2020)

## Deployment

Configured for autoscale deployment using gunicorn with UvicornWorker on port 5000.
