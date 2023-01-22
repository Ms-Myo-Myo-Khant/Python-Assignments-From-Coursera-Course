import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
js=json.loads(data)

sum=0
for item in js['comments']:
    num=int(item['count'])
    sum=sum+num
print(sum)
