# Author: Urwa Muaz, NYU, September 2018
##############################
#Code fetches the locations of all the buses of mentioned lines
##############################
# Code take two arguments
# argument one is MTA key
# argument two is Bus line
# tu run it form terminal use:
#      python show_bus_locations_um367.py <MTA key> <Busline>


# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function
# the next import allows me to read line input arguments
import sys

import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

import pandas as pd
import numpy as np
import os

# this line checks how many arguments are passed to python
# it should be a list of 3
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_um367.py <MTA key> <Busline>")
    sys.exit()

# set key
key = sys.argv[1]

#set bus
bus = sys.argv[2]

#generate url
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+key+'&VehicleMonitoringDetailLevel=calls&LineRef='+bus    

#get json data                    
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# fetch relvant data from nested json
rawBusData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# print the data
print('Bus Line: '+bus)
print('Number of Active Buses: '+str(len(rawBusData)))

busNumber = 0
for bus in rawBusData:	
    lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus '+str(busNumber)+' is at latitude '+str(lat)+' and longitude '+str(lon))
    busNumber += 1



