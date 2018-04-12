#HowOldAmI2.py
from lxml import html
import requests
import sys
import datetime


print ('')


if len(sys.argv) < 2:
    print ( 'You must pass your date of birth using YYYY/MM/dd format. Exiting....')
    exit(1)


page = requests.get("http://www.datetime.io/age/" + sys.argv[1])
tree = html.fromstring(page.content)


myage = str(tree.xpath('/html/body/div[1]/h2/span/text()')).strip('[\'').strip('\']')
dateofbith = str(tree.xpath('/html/body/div[1]/p/text()')).strip('[\'\\n\\t').strip('!\\n\']')
print ('You are ' + myage + '. ' + dateofbith)
