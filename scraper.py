from requests import get
from bs4 import BeautifulSoup as soup

url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)
html_soup = soup(response.text, 'html.parser')

movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
first_movie = movie_containers[0]
first_name = first_movie.h3.a.text
movie_titles = []

for movie in movie_containers:
    year_movie = movie.h3.find('span', class_="lister-item-year text-muted unbold").text
    rating = float(movie.strong.text)
    metascore = movie.find('span', class_="metascore")
    votes = movie.find('span', attrs = {'name': 'nv'})
    votes = int(votes['data-value'])
    
    if metascore is None:
        metascore = "No data"
    else:
        metascore = int(metascore.text)

    temp = {
        "title":movie.h3.a.text,
        "year": year_movie,
        "rating": rating,
        "metascore": metascore,
        "votes": votes
    }
    movie_titles.append(temp)

print(movie_titles)