import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import geocoder 
from geopy.geocoders import Nominatim
import descartes
from shapely.geometry import Point, Polygon


street_map = gpd.read_file('/Users/adity1/Downloads/Counties_(v17a)/Counties_(v17a).shp')
fig, ax = plt.subplots(figsize=(12,9))
street_map.plot(ax=ax)

map = geocoder.ip('me')

geoLoc = Nominatim(user_agent="GetLoc")
getLoc = geoLoc.reverse(map.latlng)
print(getLoc.address)
