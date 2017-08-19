from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.whatstheharm.net/apocalypsefear.html'
html = urlopen(url)

bsObj = BeautifulSoup(html.read(), 'html.parser')

tag = bsObj.find('cite')
print(tag.text)
