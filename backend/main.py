from fastapi import FastAPI
from scraper.scraper import scrape_product

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sneaker & PC Part Buying Bot"}

@app.get("/scrape")
def scrape(url: str):
    return scrape_product(url)
