#import json
#import requests
#import urllib3
import urllib.request
import urllib.response
#from lxml import etree
from html.parser import HTMLParser

lines = []
p = 'Hello, World!'
print(p)

class ParseMyAge(HTMLParser):
    def handle_data(self, data):
        lines = data

with urllib.request.urlopen("http://www.datetime.io/age/1989/1/1") as f:
#print(f.read().decode('utf-8'))
    p = f.read().decode('utf-8')

#print(p)

parser = ParseMyAge()
#lines = parser.feed(p)
print(lines)