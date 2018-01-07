#import json
#import requests
#import urllib3
import urllib.request
import urllib.response
#from lxml import etree
from html.parser import HTMLParser

p = 'Hello, World!'
print(p)

class ParseMyAge(HTMLParser):
    def handle_data(self, data):
        print("I am ", data)

with urllib.request.urlopen("http://www.datetime.io/age/1989/1/1") as f:
#    print(f.read().decode('utf-8'))
    p = f.read().decode('utf-8')

parser = ParseMyAge()
parser.feed(p)
