from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaTRProgramaPesquisaPrograma.asp?Exercicio=2017'
html = urlopen(base_url)

soup = BeautifulSoup(html.read(), 'html.parser')
tables = soup.findAll('table')

rows = tables[1].findAll('tr')

for row in rows:
    td = row.td

    if td:
        programa = td.text.strip()

        coluna_valor = row.find('td', { 'class': 'colunaValor' })
        valor = coluna_valor.text.strip()

        print(programa + " " + valor)
