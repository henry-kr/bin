#HowOldAmI2.py
from lxml import html
import requests

page = requests.get("http://www.datetime.io/age/1989/1/1")
tree = html.fromstring(page.content)


myage = tree.xpath('/html/body/div[1]/h2/span/text()')
print('my age: ',  myage)

#/html/body/div[12]/span
#body > div.content > h2 > span
#/html/body/table/tbody/tr[5]
#/html/body/div[1]/h2/span
#/html/body/table/tbody/tr[7]/td[2]
#/html/body/div[12]/span

#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#tree = html.fromstring(page.content)

#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

#print('Buyers: ', buyers)
#print('Prices: ', prices)