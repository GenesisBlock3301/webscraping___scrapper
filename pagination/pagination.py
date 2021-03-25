import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

titles = []
descriptions = []
authors = []
times = []
links = []


def scrap_data_by_page(webpage, page):
    print(">>>>>>>", page)
    next_page = webpage + str(page)
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all(class_="post")
    for i in range(len(items)):
        titles.append(items[i].h2.get_text().strip())
        try:
            descriptions.append(items[i].p.get_text().strip())
        except AttributeError:
            descriptions.append("Empty")
        authors.append(items[i].find(class_="theauthor").get_text().strip())
        links.append(items[i].a['href'])
        times.append(items[i].find(class_="thetime").get_text().strip())
    if page < 16:
        page += 1
        scrap_data_by_page(webpage, page)


url = 'https://www.opencodez.com/page/1'
scrap_data_by_page(url, 0)
test_df = pd.DataFrame({
    'titles': titles,
    'descriptions': descriptions,
    'authors': authors,
    'times': times,
    'links': links
})

# test_df.to_csv('single_page_data.csv')
test_df.to_csv('pagination.csv',index=False)

