import os
import requests


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    #Endereço do download   -  {} serve para colocar os padrões em seguencias tipo: _MG_01 , _MG_02 
    BASE_URL = 'endereço_url_do_arquivo_0{}.jpg'
   #Pasta para o download
    OUTPUT_DIR = 'output'  
    #Sequencia de numeros do arquivo  
    for i in range(9616, 9617):
        #Formato dos arquivos
        nome_arquivo = os.path.join(OUTPUT_DIR, 'arquivo_{}.jpg'.format(i))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo)