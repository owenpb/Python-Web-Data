import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter url: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    ##print(data.decode())

    info = json.loads(data)

    ## mylist is a list of dictionaries
    mylist = info['comments']

    total = 0
    for i in mylist:
        total = total + i['count']

    print(total)








