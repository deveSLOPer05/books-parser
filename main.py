import requests
from bs4 import BeautifulSoup as bs
#import pandas as pd

url = "https://www.chitai-gorod.ru/catalog/books-18030"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://google.com" #header взят рандомный из гугла целиком
}
r = requests.get(url, headers=headers)
#print(r.status_code)
#print(r.text)

soup = bs(r.text, "html.parser")
books_name = soup.find_all("a", class_="product-card__title")
books_price = soup.find_all("span", class_="product-mini-card-price__price product-mini-card-price__price--reverse")
for name in books_name:
    print(name["title"])
    title = name.text.strip()
for price in books_price:
    print(price.text)
