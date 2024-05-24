import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("There was an error retrieving the webpage.")

soup = BeautifulSoup(html_content, 'html.parser')
books = []

for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    books.append((title, price, availability))

print(books)
