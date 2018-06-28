from requests import get
from bs4 import BeautifulSoup as soup
import json

url = 'https://clutch.co/ca/agencies'
url_root = 'https://clutch.co'

response = get(url)
html_soup = soup(response.text, 'html.parser')

agencies_containers = html_soup.find_all('li', class_='provider-row')

agencies = []

for agency in agencies_containers:
    # we cannot get logo because it is assigned dinamically by js
    # logo_url = agency.find('div', class_="company-logo").a.img.get('src')
    company_name = agency.h3.span.a.text
    detail_url = agency.h3.span.a['href']
    detail_url = url_root + detail_url
    tagline = agency.find('p', class_="tagline").text
    test = agency.find('span', class_="rating")
    
    if agency.find('span', class_="rating") is None:
        rating = ""
    else:
        rating = float(agency.find('span', class_="rating").text)
    
    print(rating)

    temp = {
        "company_name": company_name,
        "detail_url": detail_url,
        "tagline": tagline,
        "rating": rating
    }
    agencies.append(temp)

#print(agencies)

with open('clutch.json', 'w') as my_json:
    json.dump(agencies, my_json)