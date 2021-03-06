import csv
from bs4 import BeautifulSoup
# todo firefox and chrome
from selenium import webdriver
# todo microsoft edge
from msedge.selenium_tools import Edge, EdgeOptions

# todo firefox
driver = webdriver.Firefox()


# todo chrome
# driver = webdriver.Chrome()

# todo microsoft edge
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options=options)

# url = "https://www.amazon.com/"

# driver.get(url)


def get_url(search_term):
    """Generate a URL"""
    search_term = search_term.replace(' ', '+')
    template = f"https://www.amazon.com/s?k={search_term}&ref=nb_sb_noss_2"
    return template


url = get_url("ultrawide monitor")
driver.get(url)


# print(len(results))

# todo prototype
# item = results[0]
# atag = item.h2.a
# print(atag.get_text())
# print("https://www.amazon.com/" + atag.get('href'))
# price = item.find('span', "a-price-whole").get_text()
# print(price)
# rating = item.find('span', 'a-icon-alt').get_text()
# print(rating)
# customerReview = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
# print(customerReview)


# todo Generalize the pattern
def extract_record(item):
    """Extract and return data from a single record"""
    atag = item.h2.a
    description = atag.text.strip()
    url = "https://www.amazon.com/" + atag.get('href')
    try:
        price = item.find('span', "a-price-whole").get_text()
    except AttributeError:
        return
    try:
        rating = item.find('span', 'a-icon-alt').get_text()
        customerReview = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        customerReview = ''

    result = (description, price, rating, customerReview, url)
    return result


# Extract the collection
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all('div', {'data-component-type': 's-search-result'})
records = []

for item in results:
    record = extract_record(item)
    if record:
        records.append(record)

print(records[0])