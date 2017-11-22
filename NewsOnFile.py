import requests
from bs4 import BeautifulSoup

print("#"*30)
print("#      NewsSave on File      #")
print("#  News from The Hacker News #")
print("#       @rafaelfilholm       #")
print("#"*30)
print()

def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

content = requests.get('https://hnrss.org/frontpage').content
page = BeautifulSoup(content, 'html.parser')
newsList = list(page.children)[2]

for news in newsList.find_all('item'):
    try:
        titulo = news.find('title').getText()
        nome_arquivo = chr_remove(titulo, "?:/|")
        arquivo = open(nome_arquivo+'.txt', 'r+')
        print("\033[31m Notícia Já Existe: {} \033[0;0m".format(titulo))
    except FileNotFoundError:
        arquivo = open(nome_arquivo+'.txt', 'w+')
        arquivo.write('Titulo: {}\n'.format(titulo))
        print("\033[32m Notícia Adicionada: {} \033[0;0m".format(titulo))
    arquivo.close()

print ("\033[32m Finalizado!!! \033[0;0m")

