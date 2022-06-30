#13 EX pfe - Using the google map API

import urllib.request, urllib.parse, urllib.error
import json

#note google is inc keys for the api, NEED a GOOGLE API KEY
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter locatioin: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address}
    )

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)
