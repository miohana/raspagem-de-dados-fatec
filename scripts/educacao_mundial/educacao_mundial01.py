from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://wdi.worldbank.org/table/2.7'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

# Temos duas tabelas na página contendo a classe `indicators-table`
# Os dados que queremos coletar estão na segunda tabela
tabela = soup.findAll('table', { 'class': 'indicators-table' })[1]

# Constrói uma lista contendo todas as linhas da tabela
linhas = tabela.findAll('tr')

# Cria um dicionário vazio
dict = {} 

for linha in linhas:
    pais = linha.find('td', { 'class': 'country' }).text

    # Adiciona mais uma dimensão ao nosso dicionário, desta forma
    # poderemos chamar algo como `dict[nome_do_pais][nome_da_coluna]`
    dict[pais] = {}

    # A coluna referente ao investimento é a oitava coluna da tabela (posição 7)
    investimento = linha.findAll('td')[7].text
    dict[pais]['investimento'] = investimento

print('Brasil', dict['Brazil']['investimento'])
print('Suíca', dict['Switzerland']['investimento'])
print('Alemanha', dict['Germany']['investimento'])
print('Japão', dict['Japan']['investimento'])
print('Áustria', dict['Austria']['investimento'])
