from urllib.request import urlopen
from bs4 import BeautifulSoup

pg = 0
list_elements = []

while True:
  pg += 1
  url = "http://xistarca.pt/resultados?pg={}".format(pg)
  html = urlopen(url)
  soup = BeautifulSoup(html, 'lxml')

  result_div = soup.find_all('div', class_='results-events')[0]

  next_list = result_div.find_all('a')

  if not next_list:
    break

  list_elements.extend(next_list)


for el in list_elements:
  date = el.find(class_='date').get_text()
  event = el.find(class_='event').get_text()
  url = '{}{}'.format('http://xistarca.pt', el.get('href'))
  print('{}\n{}\n'.format(event,url))
