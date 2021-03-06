from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
r = get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

movie_list = soup.find_all('div', class_='lister-item mode-advanced')
print(len(movie_list))
# first_movie = movie_list[0]
# print(first_movie.h3.a.get_text())
# print(first_movie.h3.find_all('span')[1].get_text())
# print(first_movie.find('div', class_="ratings-bar").div.strong.get_text())
# print(first_movie.find('span', class_='metascore favorable').get_text())
# print(first_movie.find('p', class_='sort-num_votes-visible').find_all('span')[1].get_text())
# print("------------------------")
dic = list()
i = 0
names = []
years = []
ratings = []
metascores = []
votes = []

for movie in movie_list:
    if movie.find('div', class_='ratings-metascore') is not None:
        name = movie.h3.a.get_text()
        names.append(name)

        year = movie.h3.find_all('span')[1].get_text()
        years.append(year)

        rating = movie.find('div', class_="ratings-bar").div.strong.get_text()
        ratings.append(float(rating))

        metascore = movie.find('span', class_='metascore').get_text()
        metascores.append(int(metascore))

        vote = movie.find('span', attrs={'name': 'nv'}).get_text()
        votes.append(int(str(vote).replace(',','')))

print(len(names), len(years), len(ratings), len(metascores), len(votes))
print(names, years, ratings, metascores, votes)
test_df = pd.DataFrame({
    'names': names,
    'years': years,
    'ratings': ratings,
    'metascores': metascores,
    'votes': votes
})

# test_df.to_csv('single_page_data.csv')
test_df.to_excel('single_page_data.xlsx')