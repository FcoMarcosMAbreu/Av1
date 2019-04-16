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
links = html.find_all(keyword)
for link in links:
    print(link[' '])


""" def search(keyword, url, deth):
    response = requests.get(url)
    print(response.text)
    pagina = BeautifulSoup(response, 'html.parser')
    ocorrencia = 0
    for keyword in pagina:
        ocorrencia+=1
        print(ocorrencia + " " + keyword + "\n") """

#print(response.status_code)
#print(response.headers['content-type'])
#print(response.text)