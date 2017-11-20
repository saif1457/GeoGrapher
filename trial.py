import urllib.parse
import requests
import json
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
