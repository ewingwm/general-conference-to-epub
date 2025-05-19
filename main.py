import requests
from bs4 import BeautifulSoup
import pypub
from pypub import *
import tempfile

def clean_html(html_text, allowed_tags):
    soup = BeautifulSoup(html_text, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name not in allowed_tags:
            tag.decompose()  # remove disallowed tags
    return str(soup)
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
        flink = 'https://www.churchofjesuschrist.org' + link.get('href')
        links.append(flink)

final_epub = pypub.Epub('General Conference April 2025')

for link in links:
    talk = requests.get(link)
    talk_text = talk.text
    # talk_text = clean_html(talk_text, {'h1', 'p', 'sup', 'head', 'title'})
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix='.html') as tmp:
        tmp.write(talk_text)
        tmp.seek(0)
        talk_chapter = create_chapter_from_file(tmp.name)
    final_epub.add_chapter(talk_chapter)

final_epub.create('./final_epub.epub')
