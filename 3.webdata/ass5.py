import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl





# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum=0
for c in counts:
    num=int(c.text)
    sum=sum+num
print(sum)
