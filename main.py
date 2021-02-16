import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com'

# step-1 get the html element
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# step 2: parse the element
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# step 3: Html tree traversal
# Commonly use type of string
# 1. Tag -> print(type(title))
# 2. bs4.element.NavigableString -> print(title.string)
# 3. BeautifulSoup object -> print(type(soup))


# Get the item of html page
title = soup.title

# get all the paragraph from page
paras = soup.find_all('p')
# print(paras)

# find all anchor tag from html
anchors = soup.find_all('a')
# print(anchors)

# get first element
print(soup.find('p'))

# Get classess of any element
print(soup.find('p')['class'])

# Find all the element with class lead
print(soup.find_all('p', class_="lead"))

print("______________________________________")
# get text from elements
print(soup.find('p').get_text())
print("__________________")
# print just text all inside all html
# print(soup.get_text())

# Get all links of page
print("=======================link==================")
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if link.get('href') != "#":
        lin = url + link.get('href')
        print(lin)
        all_links.add(lin)

print("Commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmt")
# 4. comment ->
markup = '<p><!-- this is a comment --></p>'
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

print("mark specific content")
# Mark specific content
# .content - A tag's
navSupportedContent = soup.find(id='navbarSupportedContent')
print(navSupportedContent.contents)
for ele in (navSupportedContent.stripped_strings):
    print(ele)

# difference between content and children
# .content -> a tag's children are available in list.
# .children -> a tag's are available as a generator.
