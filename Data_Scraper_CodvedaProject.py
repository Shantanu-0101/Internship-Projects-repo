import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/" 
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


titles = []
for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']  
    print(title)
    titles.append(title)
    
with open('title.csv', mode='w', newline='', encoding='utf-8')as file:
    writer = csv.writer(file)
    writer.writerow(['title'])
    for title in titles:
        writer.writerow([title])