import requests
from bs4 import BeautifulSoup

# Make request for index page
index = requests.get('https://www.churchofjesuschrist.org/study/general-conference/2025/04?lang=eng')
# Make Soup
index_soup = BeautifulSoup(index.text)
# print(index_soup.prettify())

