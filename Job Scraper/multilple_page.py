import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def get_url(position, location):
    template = "https://www.indeed.com/jobs?q={}&l={}"
    position = position.replace(" ", "+")
    location = location.replace(" ", "+")
    url = template.format(position, location)
    return url


def get_record(item):
    atag = item.h2.a
    job_title = atag['title']
    job_url = "https://www.indeed.com/" + atag.get('href')
    company_name = item.find('span', 'company').text.strip()
    location = item.find('span', {'class': 'location'}).text
    job_summary = item.find('div', {'class': 'summary'}).text.strip()
    post_date = item.find('span', {'class': 'date'}).text.strip()
    today = datetime.today().strftime('%Y-%m-%d')

    try:
        job_salary = item.find('span', {'class': 'salaryText'}).text.strip()
    except:
        job_salary = ''

    record = (job_title, company_name, location, job_salary, today, post_date, job_summary, job_url)
    return record


def main(position, location):
    records = []
    url = get_url(position, location)
    # todo Getting Next Page
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            url = "https://www.indeed.com/" + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break

        cards = soup.find_all('div', class_="jobsearch-SerpJobCard")
        for card in cards:
            record = get_record(card)
            records.append(record)
    return records


print(len(main('senior accountant', "charlotte nc")))
