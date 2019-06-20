from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.whatstheharm.net/apocalypsefear.html'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

tag = soup.cite
print(tag.text)
