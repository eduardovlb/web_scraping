from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:

    company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')

    print(f'''
    Company: {company}
    Required Skills: {skills}

    ''')