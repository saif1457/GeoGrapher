import urllib.parse
import requests
import json
import xlrd
import csv
import urllib.request, json
from shapely.geometry import shape, Point
from geopy.distance import vincenty
# depending on your version, use: from shapely.geometry import shape, Point

# load GeodataON file containing sectors
with open('countries.geo.json') as f:
    data = json.load(f)

#load the API feed
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson'
json_data = requests.get(url).json()

#Include City Risk Index cities
book = xlrd.open_workbook("cri_cities.xlsx")
cities = book.sheet_by_index(0)
us_cities = book.sheet_by_index(1)


#File Operations
headers = "title,country,mag, alert,tsunami,rangeFinder,direction,countryAffected\n"       #the col headers in csv
w = csv.writer(open("Earthquakes.csv","w")) #open file, "a" means append (add the data to the end of this file if it already exists)
w.writerow(["Title","Country","Latitude","Longitude","Magnitude","Alert","Tsunami", "Range","Direction","Country affected",])         #write them ol' headers

for x in range (1,(len(json_data["features"]))):
        title = str(json_data['features'][x]['properties']['place'])
        country = str(json_data['features'][x]['properties']['place'].split(',')[1].strip())
        Qlongitude = str(str(json_data['features'][x]['geometry']['coordinates']).split('[')[1].split(',')[0])
        Qlatitude = str(str(json_data['features'][x]['geometry']['coordinates']).split(', ')[1].split(',')[0])
        depth = str(str(json_data['features'][x]['geometry']['coordinates']).split(', ',2)[1])
        mag = str(json_data['features'][x]['properties']['mag'])
        alert = str(json_data['features'][x]['properties']['alert'])
        rangeFinder = json_data['features'][x]['properties']['place'].split('km')[0]
        direction = str(json_data['features'][x]['properties']['place'].split('km')[1].split(" of")[0])
        tsunami = str(json_data['features'][x]['properties']['tsunami'])
        mmi = json_data['features'][x]['properties']['mmi']
        sig = json_data['features'][x]['properties']['sig']
        magmax = ((pow(10, float(mag)/2))/(sig));

        #Check if country is a US state and corrects to United States of 'Murica
        for cell_row in range (1,us_cities.nrows):
            if (country == us_cities.cell_value(cell_row,0)) or (country == us_cities.cell_value(cell_row,1)):
                country = us_cities.cell_value(cell_row,2)

        #Print information for clarity and checking
        print('Title: ' + title)
        print('Country: ' + country)
        print('Longitude:' + Qlongitude)
        print('Latitude:' + Qlatitude)
        print('Depth: ' + depth)
        print('Mag: ' + mag)
        print('Alert: ' + alert)
        print ('Tsunami: ' + tsunami)
        print('Range: ' + str(rangeFinder))
        print('Direction: ' + direction)
        print ('MMI: ' + str(mmi))
        print('Sig: ' + str(sig))
        print('Max: '+ str(magmax))


        # construct point based on lon/lat returned by geocoder
        Qpoint = Point(float(Qlongitude),float(Qlatitude)).buffer(magmax)

        for feature in data['features']:
            #print (feature['geometry']['type'])
            #print (feature.geometry.type)
            polygon = shape(feature['geometry'])
            if  polygon.intersects(Qpoint) or polygon.contains(Qpoint):
                countryAffected = str((feature['properties']['name']))
                #Write to csv file
                w.writerow([title,country, Qlatitude, Qlongitude, mag,alert,tsunami,rangeFinder,direction,countryAffected])
                print ("country affected is: " + str(countryAffected))
        print('\n --------------- \n')

        for feature in data['features']:
            polygon = shape(feature['geometry'])
            if  polygon.intersects(Qpoint) or polygon.contains(Qpoint):





                f.close()        #closing the file saves it at the end of the operation, otherwise nothing would happen
