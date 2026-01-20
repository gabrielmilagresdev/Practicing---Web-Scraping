import requests
from bs4 import BeautifulSoup

#Em muitos sites de e-commerce existe um padrão de URL para busca.
#A URL abaixo é APENAS UM EXEMPLO GENÉRICO.
#Utilize apenas em sites que permitam scraping ou para fins educacionais.

url_base = "https://example.com/search?q="
product_name = input("Digite o nome do produto: ")

response = requests.get(url_base + product_name)
site = BeautifulSoup(response.text, "html.parser")

products = site.findAll("li", attrs={"class": "product-item"})

for product in products:
    product_tittle = product.find(
        "h2",
        attrs={"class": "product-title"}
    )

    product_value = product.find(
        "span",
        attrs={"class": "product-price"}
    )

    product_link = product.find(
        "a",
        attrs={"class": "product-card"}
    )

    if not (product_tittle and product_value and product_link):
        continue  #pula cards incompletos

    print("Nome do Produto: ", product_tittle.text)
    print("Valor do Produto: ", product_value.text)
    print("Link do Produto: ", product_link["href"], "\n\n")
