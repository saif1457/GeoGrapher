# GeoGrapher
<img src="http://res.cloudinary.com/dcl78rpmg/image/upload/c_scale,q_33,w_2522/v1517602325/andrew-neel-133200_wez1wd.jpg" style="width:100%"> [Photo by Andrew Neel on Unsplash](https://unsplash.com/photos/1-29wyvvLJA)







To run the script, cd into the appropriate directory and run `python GeoGrapher.py` into the command line.
  
The script goes to the United States Geological Survey (USGS) website to retrieve the geo.json file of Significant Earthquakes in the past 30 days, parsing it using `split()` function to extract:


Colons can be used to align columns.

| Extracted Data                | Notes         | To .csv          |
|-------------------------------|---------------|------------------|
| title                         |               | Title            |
| country                       |               | Country          |
| longitude                     |               | Latitude         |
| latitude                      |               | Longitude        |
| magnitude                     |               | Magnitude        |
| alert                         |               | Alert            |
| tsunami                       |               | Tsunami          |
| range                         |               | Range            |
| direction (from nearest coast |               | Direction        |
| MMI                         |               |  |
| Significance                           |  |     |
| Mag_max                            |               | Country affected |
|                               | (coming soon) | City affected    |

The script will print the logs to the command line, just as a check for the content. Using the Shapely module and the `countries.geo.json`, a point is constructed from the extracted earthquake coordinates.

Comparing each earthquake, a `for loop` runs over each point and checks whether the point intersects __or__  the country
polygon. If this is true, then it prints the country that the earthquake has affected.

Finally, the `writerow()` function prints this information in a tabular format to `Earthquakes.csv`. Note that additional running of this script overwrites previous files with the same name. To change this instead append to existing file, change the following line:

`w = csv.writer(open("Earthquakes.csv","w"))`

to

`w = csv.writer(open("Earthquakes.csv","a"))`

__"a"__ means append (add the data to the end of this file if it already exists), while __"w"__ only writes.


