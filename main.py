import requests
from bs4 import BeautifulSoup

blink = 'https://www.churchofjesuschrist.org/study/general-conference/2025/04'
# Make request for index page
index = requests.get(blink + '?lang=eng')
# Make Soup
index_soup = BeautifulSoup(index.text, 'html.parser')
# print(index_soup.prettify())

# Find all the links
links_soup = index_soup.find_all('a')
links = []
# print(links_soup)
for link in links_soup:
    name_soup = link.find_all('p', class_='subtitle-LKtQp')
    # print(name_soup)
    if(name_soup != []):
        name = str(name_soup)
        name = name.split('>')
        name = name[1]
        name = name.split()
        name = name[len(name) - 1]
        name = name.split('<')
        name = name[0]
        flink = 'https://www.churchofjesuschrist.org' + link.get('href')
        links.append(flink)
