
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

Counts = 7
Position = 18

for i in range(Counts):

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[Position - 1].get('href', None)
    print('Retrieving:', tags[Position - 1].get('href', None))
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
