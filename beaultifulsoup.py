import requests
from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com/") 
content = response.content #Salvando o conteúdo em uma variável

site = BeautifulSoup(content, "html.parser") #Convertendo o site para um objeto do beaultifulsoup. O primeiro parãmetro é o conteúdo do site, o segundo é o formato
news = site.find("div", attrs={"class" : "feed-post-body"}) #Método para procurar tags de interesse no conteúdo do site. O primeiro parâmetro é a tag e o segundo é o atributo
tittle = news.find("p", attrs={"elementtiming" : "text-ssr"})

print(tittle.text) #O .text é usado para pegar apenas o conteúdo de texto do código, sem as tags

#print(site.prettify()) #O prettify() deixa o código html de forma aninhada

