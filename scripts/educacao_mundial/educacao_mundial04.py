from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://wdi.worldbank.org/table/2.7'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

tabela = soup.findAll('table', { 'class': 'indicators-table' })[1]

linhas = tabela.findAll('tr')

dict = {} 

for linha in linhas:
    pais = linha.find('td', { 'class': 'country' }).text
    alunos_por_professor = linha.findAll('td')[11].text

    if not (alunos_por_professor == '..'):
        dict[pais] = float(alunos_por_professor) 

# Ordena de forma crescente os países conforme o número de alunos
# por professor
lista_ordenada = sorted(dict, key=dict.get)

# Itera a lista ordenada exibindo a posição ocupada por cada
# país
for nome_do_pais in lista_ordenada:
    indice = lista_ordenada.index(nome_do_pais) + 1
    print(indice, nome_do_pais, dict[nome_do_pais])

print("========================")
# Exibe a posição de um país específico na lista ordenada
print("Posição ocupada pelo Brasil:")
print(lista_ordenada.index('Brazil')+1)
