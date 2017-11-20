import urllib.parse
import requests
import json
import urllib.request, json
from shapely.geometry import shape, Point
# depending on your version, use: from shapely.geometry import shape, Point

# load GeodataON file containing sectors
with open('countries.geo.json') as f:
    data = json.load(f)

#load the API feed
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson'
json_data = requests.get(url).json()


#File Operations
filename = "earthquakes.csv"       #make a new file called ports.csv
f = open(filename,"a")          #open file, "a" means append (add the data to the end of this file if it already exists)
headers = "title,country,mag, alert,rangeFinder,direction\n"       #the col headers in csv
f.write(headers)         #write them ol' headers

for x in range (0,(len(json_data["features"]))):
        title = str(json_data['features'][x]['properties']['place'])
        country = str(json_data['features'][x]['properties']['place'].split(',')[1])
        mag = str(json_data['features'][x]['properties']['mag'])
        alert = str(json_data['features'][x]['properties']['alert'])
        rangeFinder = str(json_data['features'][x]['properties']['place'].split('km')[0])
        direction = str(json_data['features'][x]['properties']['place'].split('km')[1].split(" of")[0])


        print('Title: ' + title)
        print('Country: ' + country)
        print('Mag: ' + mag)
        print('Alert: ' + alert)
        print('Range: ' + rangeFinder)
        print('Direction: ' + direction)
        #Write to csv file
        f.write(title + "," + mag + "," + alert + "," + rangeFinder + "," + direction + "\n")


f.close()        #closing the file saves it at the end of the operation, otherwise nothing would happen



# construct point based on lon/lat returned by geocoder
point = Point(-0.118092,51.509865)
 #new york (-122.7924463, 45.4519896)
 #alice springs (133.88362,-23.69748)

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
