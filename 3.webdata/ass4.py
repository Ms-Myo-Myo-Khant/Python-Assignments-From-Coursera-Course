from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input('Enter count -'))
pos=int(input('Enter position -'))
pos=pos-1

i=0
print('Retrieving : '+url)
while i<count:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url=tags[pos].get('href', None)
    print('Retrieving : '+url)
    i=i+1
print('Last name in sequence : '+tags[pos].contents[0])
