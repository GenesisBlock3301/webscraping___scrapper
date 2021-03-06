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


url = get_url('senior accountant', "charlotte nc")
print(url)
response = requests.get(url)
# print(response.t)

soup = BeautifulSoup(response.text, 'html.parser')

cards = soup.find_all('div', class_="jobsearch-SerpJobCard")
item = cards[0]
# print(len(results))
# print(item)
atag = item.h2.a


# job_title = atag['title']
# job_url = "https://www.indeed.com/" + atag.get('href')
# company_name = item.find('span', 'company').text.strip()
# # print(company_name)
# location = item.find('span',{'class':'location'}).text
# job_summary = item.find('div',{'class':'summary'}).text.strip()
# # print(job_summary)
# post_date = item.find('span',{'class':'date'}).text.strip()
# print(post_date)
# today = datetime.today().strftime('%Y-%m-%d')
# print(today)
# # salary = item.find('span',{'class':'salaryText'}).text.strip()
# try:
#     job_salary = item.find('span',{'class':'salaryText'}).text.strip()
# except:
#     job_salary = ''
# rating = item.find('span',{'class':'ratingsContent'}).text.strip()

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


records = []

for card in cards:
    record = get_record(card)
    records.append(record)

print(records[0])
