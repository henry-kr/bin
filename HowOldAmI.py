#import whois
#import json
#import requests
#import urllib3
import urllib.request
import urllib.response
#from lxml import etree
from html.parser import HTMLParser

print ('Hello, World!')

with urllib.request.urlopen("http://www.datetime.io/age/1989/1/1") as f:
    print (f.read().decode('utf-8'))


MyAge = ParseMyAge()
MyAge.feed(f.read().decode('utf-8'))


class ParseMyAge(HTMLParser):
    def handle_data(self, data):
        print("I am ", data)