# GeoGrapher
A short script that maps geographic attributes (earthquake affected) to multiple countries/cities.
<img src="http://res.cloudinary.com/dcl78rpmg/image/upload/c_scale,q_33,w_2522/v1517602325/andrew-neel-133200_wez1wd.jpg" style="width:100%">

To run the script, cd into the appropriate directory and run `python GeoGrapher.py` into the command line.
  
The script goes to the United States Geological Survey (USGS) website to retrieve the geo.json file of Significant Earthquakes in the past 30 days, parsing it using `split()` function to extract:

title
country
longitude
latitude
depth
magnitude
alert
direction (from nearest coast)
tsunami
mmi
significance
mag_max

The script will print the logs to the command line, just as a check for the content.

Using the Shapely module, a point is constructed from the extracted earthquake coordinates.

Comparing each earthquake, a `for loop` runs over each point and checks whether the point intersects __or__  the country
polygon. If this is true, then it prints the country that the earth
