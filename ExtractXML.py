import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter url: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    ## print(data.decode())
    tree = ET.fromstring(data)

    lst = tree.findall('comments/comment')

    print('Number of users: ', len(lst))

    total = 0
    for item in lst:
        ## print(item.find('count').text)
        total = total + int(item.find('count').text)

    print('Total count: ', total)

