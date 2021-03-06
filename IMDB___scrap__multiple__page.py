from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output
from warnings import warn
import pandas as pd

names = []
years = []
ratings = []
metascores = []
votes = []

pages = [str(i) for i in range(1, 5)]
years_url = [str(i) for i in range(2000, 2018)]
# movie_list = soup.find_all('div', class_='lister-item mode-advanced')
headers = {"content-type": "text"}
start_time = time()
requests = 0

# scrape 2000-2018 value
for year_url in years_url:

    # scrap every page 1-4
    for page in pages:
        url = 'https://www.imdb.com/search/title/?release_date=' + year_url + '&sort=num_votes,desc&page=' + page
        response = get(url, headers=headers)
        sleep(randint(8, 15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
        clear_output(wait=True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break

        # parse the page with Beautiful soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # select all 50 movie container from single page
        movie_list = soup.find_all('div', class_='lister-item mode-advanced')

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
                votes.append(int(str(vote).replace(',', '')))

# print(len(names), len(years), len(ratings), len(metascores), len(votes))
# print(names, years, ratings, metascores, votes)
data_df = pd.DataFrame({
    'names': names,
    'years': years,
    'ratings': ratings,
    'metascores': metascores,
    'votes': votes
})

data_df.to_excel('multi-page.xlsx')
