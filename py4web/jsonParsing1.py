import urllib.request,urllib.parse, urllib.error
import json

url=input('Enter URL:')
fhand=urllib.request.urlopen(url).read().decode()

#craeting json from from
js=json.loads(fhand)
l=js['comments']
sum=0
for i in l:
    sum+=int(i['count'])
print(sum)    
