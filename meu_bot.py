
# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
from contatos  import lista_de_usuarios
from mensagem_promocional import mensagem_examedevista, link_facebook
from lista_nomes import nomes

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")
sleep(3)
for agenda, primeiroNome in zip(lista_de_usuarios, nomes):
    wp.search_contact(agenda)
    sleep(3)
    mensagem = f'Olá {primeiroNome} quem fala é o Jonatas da Ótica Souza Costa.'
    wp.send_message(mensagem)
    sleep(2)
    wp.send_message(mensagem_examedevista)
    sleep(2)
    wp.send_message(link_facebook)
    sleep(2)

sleep(10)
wp.driver.close()
