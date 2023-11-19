 import urllib.request, urllib.parse, urllib.error
import json
serviceur1 = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
 adreess =input("Enter location: ")
 if len(address) < 1: break
 url1 = serviceur1 + urllib.parse.urlencode({'adress' : address})

 print('Retrieved',url)
 uh = urllib.requst.urlopen(url)
 data = uh.read(),decode()
 print('retrieved',len(data),'characters')

 try:
   
   js = json.loads(data)
 expect:
 js = None
 if not js or 'status' not in js or js['status'] != 'ok' :
  print('===failure to retrieve ===')
  print(data)
  continue
 lat =js["results[0],["geomestry"]["location"]["lat"]
 ing =js["results[0],["geomestry"]["location"]["lat"]
 print('lat' ,lat,'ing,ing')
 location = js[results'][0]['formatted_adress']
               print(location)



