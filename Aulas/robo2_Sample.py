from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

# Atribução de variáveis
email = "seu e-mail"
senha = "sua senha"
destinatario = "e-mail destinatário"
assunto = "E-mail do robô"
mensagem = "Olá!\nEsta mensagem foi enviada por um robô\nMensagem com um pouco de texto para verificar a velocidade com que o robô irá escrever"

driver = webdriver.Chrome('C:\\cursosUdemy\\robos_python\\chromedriver')

campoEmail = ''
campoSenha = ''
campoAssunto = ''
campoPara = ''
campoMsg = ''
btnEnviar = ''
print("Inciando robô...\n")

print("Acessando o G-mail")

driver.get("https://gmail.com.br")

print("Realizando Login")
campoEmail = driver.find_element_by_id('identifierId')
campoEmail.clear()
campoEmail.send_keys(email)
campoEmail.send_keys(Keys.RETURN)
time.sleep(2)
campoSenha = driver.find_element_by_name('password')
campoSenha.clear()
campoSenha.send_keys(senha)
campoSenha.send_keys(Keys.RETURN)

print("Login Realizado")

print("Abrindo caixa de e-mail")
time.sleep(3)
driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(1)

campoPara = driver.find_element_by_name('to')
campoPara.clear()
campoPara.send_keys(destinatario)
campoPara.send_keys(Keys.RETURN)

campoAssunto = driver.find_element_by_name('subjectbox')
campoAssunto.clear()
campoAssunto.send_keys(assunto)
campoAssunto.send_keys(Keys.RETURN)

campoMsg = driver.find_element_by_id(':r9')
campoMsg.clear()
campoMsg.send_keys(mensagem)
campoMsg.send_keys(Keys.RETURN)

btnEnviar = driver.find_element_by_id(':pu')
btnEnviar.send_keys(Keys.RETURN)
# driver.close()

