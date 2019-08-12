from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pdb
import xlrd

print("Iniciando Robô... \n")

dominios = []
arqTxt = ''
texto = ''
#Lendo do EXCEL
arquivo = xlrd.open_workbook('C:\\cursosUdemy\\robos_python\dominios.xlsx')
sheet = arquivo.sheet_by_index(0) #le os dados da primeira aba do excel
for linha in range(0,12):
    dominios.append(sheet.cell_value(linha,0))


driver = webdriver.Chrome('C:\\cursosUdemy\\robos_python\\chromedriver')# Localiza onde está o driver do chrome
driver.get('https://registro.br/') # acessa o site no navegador

arqTxt = open('C:\\cursosUdemy\\robos_python\\result.txt','w')
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")  # encontra o input pelo ID
    pesquisa.clear()  # limpa o input caso tenha algo nele
    pesquisa.send_keys(dominio)  # escreve no imput
    pesquisa.send_keys(Keys.RETURN) # aperta a tecla ENTER
    time.sleep(2) #utilizar em casos que não de tempo da tela renderizar por completo
    resultados = driver.find_elements_by_tag_name("strong")  # encontra pela TAG HTML
    # pdb.set_trace() # para o programa para efetuar a interação
    texto = "Domínio %s %s" % (dominio, resultados[4].text +'\n') # porcentagem é igual a variável, em sua respectiva ordem
    arqTxt.write(texto)
    
arqTxt.close()
driver.close()
