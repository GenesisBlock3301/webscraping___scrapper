from requests import get
from bs4 import BeautifulSoup

url = 'https://www.socialbakers.com/statistics/facebook/pages/total/afghanistan/brands/page-3-7'

r = get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())