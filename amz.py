from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com.br/Box-Trilogia-Senhor-dos-An%C3%A9is/dp/8595086354/ref=sr_1_2?dchild=1&keywords=senhor+dos+aneis&qid=1616163651&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

produto = soup.find(id='productTitle').get_text()
preco = soup.find(class_='offer-price').get_text()

print(f'Produto: {produto}')
print(f'Preço: {preco}')

print("Funcionando")