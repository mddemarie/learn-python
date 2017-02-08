from urllib2 import urlopen
from json import loads, dumps

url = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = raw_input('Enter location: ')
url = url + '&sensor=false&address=' + address
print 'Retrieving', url

response = urlopen(url)
data = response.read()
print 'Retrieved', len(data), 'characters'

js = loads(data)
print dumps(js, indent=4)

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print 'lat', lat, 'lng', lng
location = js["results"][0]["formatted_address"]
print location