#HowOldAmI2.py
from lxml import html
import requests
import sys
import datetime

#page = requests.get("http://www.datetime.io/age/1989/1/1")
#tree = html.fromstring(page.content)

print ('')

#birthdate = datetime.datetime.strptime(sys.argv[1], %y)  #(sys.argv[1]) #+ '/' + datetime.date.month(sys.argv[1]) + '/' + datetime.date.day(sys.argv[1])
#print (birthdate)
#if not isinstance(birthdate, datetime(datetime.date)):
#    print ('You must pass a valid birth date. Exiting...')
#    exit(1)

if len(sys.argv) < 2:
    print ( 'You must pass your date of birth. Exiting....')
    exit(1)


page = requests.get("http://www.datetime.io/age/" + sys.argv[1])
tree = html.fromstring(page.content)


myage = str(tree.xpath('/html/body/div[1]/h2/span/text()')).strip('[\'').strip('\']')
dateofbith = str(tree.xpath('/html/body/div[1]/p/text()')).strip('[\'\\n\\t').strip('!\\n\']')
print ('You are ' + myage + '. ' + dateofbith)

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