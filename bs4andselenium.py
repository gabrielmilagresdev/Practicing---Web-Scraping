import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options #Importando biblioteca para alterar as configurações do navegador
from selenium.webdriver.common.keys import Keys #Importando biblioteca para conseguir utilizar as teclas do teclado
from time import sleep 

options = Options() #Instanciando um objeto options
options.add_argument("window-size=800,800")
options.add_argument("--headless") #Para executar os métodos sem abrir uma janela do browser

print("Acessando site...")
browser = webdriver.Chrome(options=options) #Passando o objeto como parâmetro para inserir as configurações alteradas
browser.get("https://www.google.com.br/travel/") 

sleep(1) #Esperando dois segundos para a página renderizar e conseguir pegar informações do código fonte

city = input("Qual local deseja visitar?: ")
print("Buscando...")

#Fazendo as rotinas para entrar na aba de hoteis
input_place = browser.find_element(By.TAG_NAME,"input")
input_place.send_keys("hotel em "+city)
sleep(0.5)
input_place.send_keys(Keys.RETURN)
sleep(0.5)
input_enter = browser.find_element(By.TAG_NAME,"li")
input_enter.click()
sleep(5)

content = browser.page_source #Atributo que contém o código fonte da página
site = BeautifulSoup(content, "html.parser") #Transformando o código fonte em um objeto do bs4
page = 1

'''
with open("arquivo.txt", "w", encoding="utf-8") as arquivo: #Escrevendo o site em um arquivo txt
    arquivo.write(site.prettify())
'''

hotels = site.find_all("div", attrs={"class": "uaTTDe BcKagd bLc2Te Xr6b1e"})
hotel_amout = site.find("div", attrs={"class": "GDEAO"})
print(hotel_amout.text + " encontrados")
number_hotels = int(''.join(c for c in hotel_amout.text if c.isdigit()))

while(True):
    search_amout = int(input("Quantos hotéis deseja procurar?: "))
    if(search_amout <= number_hotels):
        break
    print("Número superior ao de hotéis encontrados!")
rest = search_amout
count = 0
print("Buscando...")

with open("hotels.txt", "w", encoding="utf-8") as arquivo:
    while(True):
        new_content = browser.page_source
        new_site = BeautifulSoup(new_content, "html.parser")
        hotels = new_site.find_all("div", attrs={"class": "uaTTDe BcKagd bLc2Te Xr6b1e"})
        for hotel in hotels:
            hotel_name = hotel.find("a", attrs={"class": "PVOOXe"})
            hotel_value = hotel.find("span", attrs={"class": "qQOQpe prxS3d"})
            hotel_rating = hotel.find("span", attrs={"class": "ta47le"})
            hotel_link = hotel.find("a", attrs={"class": "PVOOXe"})

            if not (hotel_name):
                nome = "Nome não informado"
            else:
                nome = hotel_name.get("aria-label", "N/A")

            if not (hotel_value):
                valor = "Valor não informado"
            else:
                valor = hotel_value.text.strip()

            if not (hotel_rating):
                avaliacao = "Sem avaliações"
            else:
                avaliacao = hotel_rating.text.strip()

            if not (hotel_link):
                link = "Link não encontrado"
            else:
                link = "https://google.com.br" + hotel_link.get("href", "")

            if not(hotel_name or hotel_value or hotel_rating or hotel_link):
                continue
            else:
                count+=1

            '''
            print("Nome do Hotel:", nome)
            print("Valor da Diária:", valor)
            print("Avaliação do Hotel:", avaliacao)
            print("Link do Hotel:", link, "\n")
            '''

            arquivo.write(f"Nome do Hotel: {nome}\n")
            arquivo.write(f"Valor da Diária: {valor}\n")
            arquivo.write(f"Avaliação do Hotel: {avaliacao}\n")
            arquivo.write(f"Link do Hotel: {link}\n")
            arquivo.write("-" * 40 + "\n")
            if(count == search_amout):
                break
        rest = rest - 20
        if(count == search_amout):
            break
        sleep(1)
        if(rest > 20):
            if page == 1:
                next = browser.find_element(By.CLASS_NAME, "eGUU7b")
                next.click()
            elif page > 1:
                next = browser.find_element(By.CLASS_NAME, "eGUU7b")
                next_button = next.find_element(By.XPATH, ".//button[2]")
                next_button.click()
        page+=1
        sleep(5)
print("Escrevendo em hotels.txt...")
sleep(2)
print("Acesso concluído.")
if(count == 0):
    print("Nenhum hotel encontrado.")
#input("Pressione ENTER para fechar o navegador...")
browser.quit()


