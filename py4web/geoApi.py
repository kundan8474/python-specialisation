import urllib.request,urllib.parse,urllib.error
import json

serviceurl="http://py4e-data.dr-chuck.net/geojson?"
addr=input("Enter address: ")
url=serviceurl + urllib.parse.urlencode({'address':addr})

data=urllib.request.urlopen(url).read().decode()
js=json.loads(data)

if not js or 'status' not in js or js['status']!='OK':
    print('not a valid response')
    quit()

print(js['results'][0]['place_id'])
