from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

@app.get("/search_pubmed")
def search_pubmed(query: str = Query(..., description="Medical question or keyword")):
    # Search for PubMed articles matching the query
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 1
    }
    search_resp = requests.get(PUBMED_SEARCH_URL, params=search_params).json()
    pmids = search_resp.get("esearchresult", {}).get("idlist", [])
    if not pmids:
        return {"error": "No results found."}
    pmid = pmids
    # Get abstract for the first PubMed article
    fetch_params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "text",
        "rettype": "abstract"
    }
    fetch_resp = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    return {"pmid": pmid, "abstract": fetch_resp.text.strip()}

