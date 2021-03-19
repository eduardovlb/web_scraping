from selenium.webdriver import Chrome
from time import sleep


url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Chrome()

navegador.get(url)

sleep(3)

a = navegador.find_element_by_tag_name('a')
p = navegador.find_element_by_tag_name('p')

print(f'Texto de a: {a.text}')
print(f'Texto de p: {p.text}')

#navegador.quit()