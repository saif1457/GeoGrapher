import urllib.request, json
from shapely.geometry import shape, Point
# depending on your version, use: from shapely.geometry import shape, Point

# load GeodataON file containing sectors
with open('countries.geo.json') as f:
    data = json.load(f)

# construct point based on lon/lat returned by geocoder
point = Point(-0.118092,51.509865)
 #new york (-122.7924463, 45.4519896)
 #alice springs (133.88362,-23.69748)

'''
for feature in data['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        #print ('Found containing polygon:' + feature)
        print (str(len(data['features'])))
        #print ('Found containing polygon:' + str(data['feature'][0]['properties']['name']))
        #print ('Found containing polygon:' + str(data['features'][0]['properties']['name']))

        break
dist = Point(0,0).distance(Point(1,1))
print(dist)
dist = Point(133.88362,-23.69748).distance(Point(-122.7924463, 45.4519896))
print(str(dist) + "km")
for feature in data['features']:
    feature['geometry']['coordinates'] = [[
        [[long, lat] for lat, long in coords] for coords in poly]
        for poly in feature['geometry']['coordinates']]
'''

#LONG / LAT
from geopy.distance import vincenty
#geolocator = Nominatim()
#work = geolocator.geocode("1 Lime Street London")
#home = geolocator.geocode("2420 Campus Drive Evanston")
newyork = (40.730610,-73.935242)
london = (51.509865,-0.118092)
#print (work.address)
#print (home.address)
#print(vincenty((home.latitude,home.longitude), (work.latitude,work.longitude)).miles)
print(str(vincenty(newyork, london).miles)  + " miles")


# check each polygon to see if it contains the point


#for y in range (0,(len(data['features']))):
for feature in data['features']:
    #print (feature['geometry']['type'])
    #print (feature.geometry.type)
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        found = (feature['properties']['name'])
        print ("country affected is: " + str(found))
        #countryAffected = str(data['features'][found]['properties']['id'])
        #print ("country affected is: " + countryAffected)
        #print ('Found containing polygon:' + str(feature))
        break
