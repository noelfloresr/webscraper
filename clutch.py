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
    testimonials = agency.blockquote.p.text
    provider_detail = agency.find('div', class_="provider-info__details")
    provider_detail_items = provider_detail.find_all('div', class_="list-item")
    min_project_size = provider_detail_items[0].text
    employees = provider_detail_items[2].span.text
    location = provider_detail_items[3].text
    nav_right_profile = agency.find('div', class_="provider-link-details").ul
    nav_right_profile = nav_right_profile.find_all('li')
    website_url = nav_right_profile[0].a.get('href')
    # we cannot access to email address
    # contact_list = nav_right_profile[2].find('div', class_="contact-dropdown").find_all('div', class_="item")
    # profile_email = contact_list[0].a['href']
    # print(profile_email)
    # We cannot access to service focus, it is generates by js library
    # chart_container = agency.find('div', class_="chartAreaContainer")

    service_focus = []

    if provider_detail_items[1].span is None:
        hourly_rate = "Undisclosed"
    else:
        hourly_rate = provider_detail_items[1].span.text
    
    # if there is not rating data
    if agency.find('span', class_="rating") is None:
        rating = ""
    else:
        rating = float(agency.find('span', class_="rating").text)

    # if there is not reviews
    if agency.find('span', class_="reviews-count") is None:
        reviews = 0
    else:
        reviews = agency.find('span', class_="reviews-count").text
        reviews = reviews.split(' ')[0]

    if agency.find('div', class_="provider-info__description").ul is None:
        author = ""
    else:
        author = agency.find('div', class_="provider-info__description").ul.li.text
    
    # print(grid)

    agency_dictionary = {
        "company_name": company_name,
        "detail_url": detail_url,
        "tagline": tagline,
        "rating": rating,
        "reviews": reviews,
        "testimonials": testimonials,
        "author": author,
        "min_project_size": min_project_size,
        "hourly_rate": hourly_rate,
        "employees": employees,
        "location": location,
        "website": website_url
    }
    agencies.append(agency_dictionary)

#print(agencies)

with open('clutch.json', 'w') as my_json:
    json.dump(agencies, my_json)