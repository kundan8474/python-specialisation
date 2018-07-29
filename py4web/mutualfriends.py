# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def retSoup(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

count=int(input('Enter count'))
pos=int(input('Enter position'))
url=input('url -')

for i in range(count):
    soup=retSoup(url)
    tags = soup('a')
    l=list()
    n=list()
    for tag in tags:
        l.append(tag.get('href', None))
        n.append(tag.contents[0])
    url=l[pos-1]
    name=n[pos-1]
print(name)
