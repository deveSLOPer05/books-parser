import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

file_name = "books.csv"

def parse():
    url_template = "https://www.chitai-gorod.ru/catalog/books-18030"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://google.com" #header взят рандомный из гугла целиком
    }
    result_list = {"link":[], "title":[], "price":[]}
    r = requests.get(url_template, headers=headers)
    #print(r.status_code)
    #print(r.text)

    soup = bs(r.text, "html.parser")
    books_name = soup.find_all("a", class_="product-card__title")
    books_price = soup.find_all("span", class_="product-mini-card-price__price product-mini-card-price__price--reverse")
    for name in books_name:
        result_list["link"].append("https://www.chitai-gorod.ru"+name.get("href"))
        result_list["title"].append(name.text.strip())
    for price in books_price:
        result_list["price"].append(price.text)
    return result_list

df = pd.DataFrame(data=parse())
df.to_csv(file_name, sep="\t", index=False, encoding="utf-8-sig") #для красивого вида в экселе при импорте нужно указать знак табуляции как "символ-разделитель"
print("данные сохранены")