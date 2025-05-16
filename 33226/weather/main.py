import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCwSCSi2A6y9umRY2YWkPWkm3yCRL2kKAY')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

print(geocode_result)