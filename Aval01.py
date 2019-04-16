from bs4 import BeautifulSoup
import requests

# keyword = 'instituto'
keyword = 'github'
# url = 'http://www.ifpi.edu.br/'
url = 'http://pages.github.com/'
deth = 4

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
ocorrencia = 0
for palavra in html:
    oc = palavra.find(keyword)
    ocorrencia+=1
    o = str(ocorrencia)
    print(o, palavra, '\n')

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