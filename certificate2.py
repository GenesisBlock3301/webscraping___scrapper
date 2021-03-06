from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.apca.org/certifications-examinations/cbnc-and-cbcct/'

r = get(url)
soup = BeautifulSoup(r.content, 'html.parser')
tr_list = soup.find('div',class_="menu-footer-col-2-menu-container")
print("val",tr_list)

cert_names = []
cert_urls = []
cert_master_urls = []
company_urls = []
companies = []
# for i in range(len(tr_list)):
#     cert_name = tr_list[i].find('h4').get_text()
#     # print(cert_name)
#     cert_url = tr_list[i].find('a').get('href')
#     cert_master_url = "https://edu.alibabacloud.com/certification?spm=a3c0i.14527127.4363105600.4.7a7136adMfCj1J"
#     company_url = "https://edu.alibabacloud.com/"
#     company = "alibabacloud"
#     cert_names.append(cert_name)
#     cert_urls.append(cert_url)
#     cert_master_urls.append(cert_master_url)
#     company_urls.append(company_url)
#     companies.append(company)

# test_df = pd.DataFrame({
#     'cert_names': cert_names,
#     'cert_urls': cert_urls,
#     'cert_master_urls': cert_master_urls,
#     'company_urls': company_urls,
#     'companies': companies
# })
# test_df.to_csv('certificate.csv',mode='a',index = False)
