import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url="http://py4e-data.dr-chuck.net/comments_112246.xml"
data=urllib.request.urlopen(url).read()
tree=ET.fromstring(data.decode())
l=tree.findall('comments/comment')
sum=0
for i in l:
    num=i.find('count').text
    sum+=int(num)
print(sum)
