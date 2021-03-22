from bs4 import BeautifulSoup
import requests

url = 'https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

dias = soup.find_all('div', class_='date-inside-circle')

lista_dias = []

for dia in dias:
    lista_dias.append(dia.text.replace('\n', ' '))

print(lista_dias)

infos = soup.find('div', class_='card').find_all('div', class_='_margin-l-5', limit=10)

dados = []

#print(infos)

#n, j = enumerate(infos)

for i, j in enumerate(infos):
    for n in j:
        a = j.find_all('span')
    for s in a:
        dados.append(s.text)

print(dados)

"""

for n, info in enumerate(infos):
        for i in range(7):
            dados[n][i].append(info)

print(dados)

"""
print("Ok")