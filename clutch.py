from requests import get
from bs4 import BeautifulSoup as soup
import json

url = 'https://clutch.co/ca/agencies'

response = get(url)
html_soup = soup(response.text, 'html.parser')

agencies_containers = html_soup.find_all('li', class_='provider-row')

agencies = []

for agency in agencies_containers:
    company_name = agency.h3.span.a.text

    temp = {
        "company_name": company_name
    }
    agencies.append(temp)

print(agencies)

with open('clutch.json', 'w') as my_json:
    json.dump(agencies, my_json)