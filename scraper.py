import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for page in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("article", class_="product_pod")

    for item in items:
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        availability = item.find("p", class_="instock availability").text.strip()
        rating = item.find("p")["class"][1]

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)

print(f"Scraped {len(df)} books successfully!")
