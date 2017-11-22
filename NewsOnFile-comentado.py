import requests # importa a biblioteca de requisicoes http
from bs4 import BeautifulSoup # importa a  biblioteca que irá tratar o retorno

print("#"*30)
print("#      NewsSave on File      #")
print("#  News from The Hacker News #")
print("#       @rafaelfilholm       #")
print("#"*30)
print()

#funcao para remover caracteres invalidos para criar o arquivo
def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

# faz a requisicao ao site que retorna com noticias do The Hacker News...
# ultilizando a funcao get() da biblioteca requests e pega o conteudo da requisicao .content
content = requests.get('https://hnrss.org/frontpage').content

# chama a funcao BeautifulSoup da biblioteca Beautiful...
# passando como primeiro parametro a variavel contendo o resultado da requisicao... 
# e segundo parametro informando pra analisar o conteudo html
page = BeautifulSoup(content, 'html.parser')

# recebe as tags filhas(children) do indice 2 da tupla([2] - corpo da pagina)...
# atribuindo as tags, no caso noticias, a variavel newsList
newsList = list(page.children)[2]

# percorre toda a lista e busca por tags nomeadas 'item'(newsList.find_all('item'))...
# 'item' é como estao dividas as noticias na pagina da requisicao

for news in newsList.find_all('item'):
    # tenta(try)
    try:
        titulo = news.find('title').getText() # dentro da noticia(news) pesquisa pela tag de titulo(find('title')) e obtem seu conteudo(.getText())
        nome_arquivo = chr_remove(titulo, "?:/|") # nome do arquivo sera o seu titulo sem nenhum caractere especial
        arquivo = open(nome_arquivo+'.txt', 'r+') # abre o arquivo para leitura
        print("\033[31m Notícia Já Existe: {} \033[0;0m".format(titulo)) # se tudo der certo printa um aviso de que a noticia ja existe
    # se der erro de arquivo nao encontrado, ou seja, noticia nao existe
    except FileNotFoundError:
        arquivo = open(nome_arquivo+'.txt', 'w+') # abre o arquivo para escrita
        arquivo.write('Titulo: {}\n'.format(titulo)) # escreve no arquivo o titulo
        print("\033[32m Notícia Adicionada: {} \033[0;0m".format(titulo)) # exibe o nome da noticia informando que foi criada com sucesso
    arquivo.close() # fecha o arquivo

print ("\033[32m Finalizado!!! \033[0;0m")
