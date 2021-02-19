from fastapi import FastAPI
from app.api.ner import ner
from spacy.cli import download
download("en_core_web_sm", direct=False)

app = FastAPI(openapi_url="/api/v1/ner/openapi.json", docs_url="/api/v1/ner/docs")

app.include_router(ner, prefix="/api/v1/ner", tags=["ner"])
