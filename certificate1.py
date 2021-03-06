from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.talend.com/academy/certification/?fbclid=IwAR1VmUHG3eUdXjSZNxldfA4HBh7cM59rEyvg6mGaBL04BmNRzxrlNZpgbAk'

r = get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
tr_list = soup.find_all('tr')
# cert_name = tr_list[1].find('a').get_text()
# print(cert_name)
# cert_url = tr_list[1].find('a').get('href')
# print(cert_url)
cert_master_url = "https://www.talend.com/academy/certification/"
cert_names = []
cert_urls = []
cert_master_urls = []
company_urls = []
companies = []
for i in range(1, 7):
    cert_name = tr_list[i].find('a').get_text()
    cert_url = tr_list[i].find('a').get('href')
    cert_master_url = "https://www.talend.com/academy/certification/"
    company_url = "https://www.talend.com/"
    company = "talend"
    cert_names.append(cert_name)
    cert_urls.append(cert_url)
    cert_master_urls.append(cert_master_url)
    company_urls.append(company_url)
    companies.append(company)

test_df = pd.DataFrame({
    'cert_names': cert_names,
    'cert_urls': cert_urls,
    'cert_master_urls': cert_master_urls,
    'company_urls': company_urls,
    'companies': companies
})
test_df.to_csv('certificate.csv',mode='a' ,index = False)
