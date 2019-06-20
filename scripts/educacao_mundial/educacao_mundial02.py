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

    dict[pais] = {}

    investimento = linha.findAll('td')[7].text
    dict[pais]['investimento'] = investimento

    # Adiciona a coluna referente a taxa de alunos por professor
    # no ensino primário. Troque a posição 11 por 12 caso deseje
    # considerar o ensino secundário.
    alunos_por_professor = linha.findAll('td')[11].text
    dict[pais]['alunos_por_professor'] = alunos_por_professor

print('Brasil', dict['Brazil']['investimento'], dict['Brazil']['alunos_por_professor'])
print('Suíca', dict['Switzerland']['investimento'], dict['Switzerland']['alunos_por_professor'])
print('Alemanha', dict['Germany']['investimento'], dict['Germany']['alunos_por_professor'])
print('Japão', dict['Japan']['investimento'], dict['Japan']['alunos_por_professor'])
print('Áustria', dict['Austria']['investimento'], dict['Austria']['alunos_por_professor'])
