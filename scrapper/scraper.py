import requests
from bs4 import BeautifulSoup

def scrape_bestbuy_computer(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # Mimic a real browser request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product title
        title = soup.find("h1").text.strip() if soup.find("h1") else "Title not found"

        # Extract price
        price_elem = soup.select_one(".priceView-hero-price.priceView-customer-price span")
        price = price_elem.text.strip() if price_elem else "Price not found"

        # Extract availability (in stock, out of stock)
        availability_elem = soup.select_one(".availabilityMessage_")
        availability = availability_elem.text.strip() if availability_elem else "Availability not found"

        # Extract key specifications
        specs = {}
        specs_container = soup.select(".column_6 .row")  # Locate specification table
        for spec in specs_container:
            key = spec.select_one(".label").text.strip() if spec.select_one(".label") else None
            value = spec.select_one(".value").text.strip() if spec.select_one(".value") else None
            if key and value:
                specs[key] = value

        return {
            "title": title,
            "price": price,
            "availability": availability,
            "specs": specs
        }
    else:
        return {"error": "Failed to fetch the page", "status_code": response.status_code}

if __name__ == "__main__":
    test_url = "https://www.bestbuy.com/site/apple-macbook-air-13-6-laptop-apple-m2-chip-8gb-memory-256gb-ssd-starlight/6509650.p?skuId=6509650"
    print(scrape_bestbuy_computer(test_url))
