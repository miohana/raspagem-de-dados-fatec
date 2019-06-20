import sys
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.fatecjd.edu.br/portal/sobre-nos/corpo-docente/'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

body = soup.tbody
rows = body.findAll('tr')

for row in rows:
    name = row.td.text

    if sys.argv[1].upper() in name:
        text = row.text

print(f"""
As informações disponíveis no site da Fatec para este(a) professor(a) são:

{text.strip()}

Um e-mail rascunho para este destinatário será criado a partir da sua conta.
""")

report = { 'value1': text }

event_name = 'nome_do_evento'
key = 'chave_webhook'

path = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{key}"
requests.post(path, data=report)
