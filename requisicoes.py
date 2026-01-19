import requests #Biblioteca para fazer as requisições

response = requests.get("https://quotes.toscrape.com/") #A variável response contém a resposta da requisição do site pelo método get
print("Status Code:", response.status_code) #O atributo status_code retorna os status da requisição (2XX - Sucesso, 4XX - Erro Cliente, 5XX - Erro Servidor ...)
print("Header: \n", response.headers) #Retorna informações do servidor
print("Content: \n", response.content) #Retorna o conteúdo do site