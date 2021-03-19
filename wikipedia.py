from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.h1
body = soup.find('div', class_='mw-parser-output').p

print(f'Título: {title.get_text()}')
print(f'Corpo: {body.get_text()}')

print("Funcionando")