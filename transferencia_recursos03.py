from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaTRProgramaPesquisaPrograma.asp?Exercicio=2017'
html = urlopen(base_url)

bsObj = BeautifulSoup(html.read(), 'html.parser')

pag = bsObj.find('p', { 'class': 'paginaAtual'})
total_pages = int(pag.text[-1])
programa_valor = {}

for page in range(total_pages):
    page += 1
    url = base_url + '&Pagina=' + str(page)
    html = urlopen(url)

    bsObj = BeautifulSoup(html.read(), 'html.parser')
    tables = bsObj.findAll('table')

    rows = tables[1].findAll('tr')

    for row in rows:
        td = row.find('td')

        if td:
            programa = td.text.strip()

            coluna_valor = row.find('td', { 'class': 'colunaValor' })
            valor = coluna_valor.text.strip()
            
            valor = float(valor.replace('.', '').replace(',', '.'))
            programa_valor[programa] = valor

print('Os cinco programas que receberam mais recursos:')
programas = sorted(programa_valor, key=programa_valor.get, reverse=True)[:5]
for programa in programas:
    print(programa, programa_valor[programa])

print('---------------------')

print('Os cinco programas que receberam menos recursos:')
programas = sorted(programa_valor, key=programa_valor.get)[:5]
for programa in programas:
    print(programa, programa_valor[programa])

print('---------------------')

print('Total transferido')
print(sum(programa_valor.values()))

print('---------------------')

print('Programas que contenham a palavra Educação ordenados por valor')
for key in sorted(programa_valor, key=programa_valor.get, reverse=True):
    if 'Educação' in key:
        print(key)
        print(programa_valor[key])
