import csv
from bs4 import BeautifulSoup
# todo firefox and chrome
from selenium import webdriver
# todo microsoft edge
import asyncio
from msedge.selenium_tools import Edge, EdgeOptions

records = []


def get_url(search_term):
    """Generate a URL"""
    search_term = search_term.replace(' ', '+')
    url = f"https://www.amazon.com/s?k={search_term}&ref=nb_sb_noss_2"

    # todo add query parameter
    url += '&page{}'
    return url


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


async def main(search_term):
    """Run main program routine"""
    # todo startup the web driver
    # todo firefox
    driver = webdriver.Firefox()
    url = get_url(search_term)
    driver.get(url)
    for page in range(1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    driver.close()

    await asyncio.sleep(0.1)
    print(records)

    # with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['Description', 'Price', 'Rating', 'CustomerReview', 'Url'])
    #     writer.writerows(records)


if __name__ == '__main__':
    asyncio.run(main('ultrawide monitor'))
