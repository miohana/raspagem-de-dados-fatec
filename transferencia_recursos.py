from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaTRProgramaPesquisaPrograma.asp?Exercicio=2017'
html = urlopen(base_url)

bsObj = BeautifulSoup(html.read(), 'html.parser')

pag = bsObj.find('p', { 'class': 'paginaAtual'})
total_pages = int(pag.text[-1])

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

            print(programa + " " + valor)
