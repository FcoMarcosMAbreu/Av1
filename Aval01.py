from bs4 import BeautifulSoup
import requests
import re

# keyword = 'instituto'
keyword = 'jekill'
# url = 'http://www.ifpi.edu.br/'
url = 'http://pages.github.com/'
deth = 4

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
links = html.find_all('a')
for link in links:
    print(link['href'])