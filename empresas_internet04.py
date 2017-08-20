from urllib.request import urlopen
from bs4 import BeautifulSoup
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

url = 'http://www.worldatlas.com/articles/the-25-largest-internet-companies-in-the-world.html'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

tbody = soup.tbody

linhas = tbody.findAll('tr')

setores = []

for linha in linhas:
    setor = linha.findAll('td')[2].text.lower()
    setores.append(setor)

tabela_frequencias = stats.itemfreq(setores)

frequencias = tabela_frequencias[:, 1].astype(int)
xi = tabela_frequencias[:, 0]

fig = plt.figure(1)
x_pos = np.arange(len(xi))
plt.bar(x_pos, frequencias, align='center')
plt.ylim(0, max(frequencias)+0.5)
plt.xticks(np.arange(len(xi)), xi, rotation='vertical')
fig.autofmt_xdate()
fig.savefig('frequencies.png')
