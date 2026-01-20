from selenium import webdriver #Importando o webdriver
from selenium.webdriver.common.by import By #Importando o By para identificar o elemento HTML ao selenium
from time import sleep #Importando o Sleep para ter algumas pausas durante o acesso ao site

browser = webdriver.Chrome() #Método para abrir o navegador

browser.get("https://www.example.com.br/") #Para acessar uma URL

search = browser.find_element(By.ID, "search") #Acessar um input pelo ID

sleep(5) #Espera 5 segundos

search.send_keys("product") #Escrever algo no search
 
input("Pressione ENTER para fechar o navegador...") #Para o navegador ficar aberto