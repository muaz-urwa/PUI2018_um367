#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Urwa Muaz, NYU, September 2018
##############################
# Code fetches the locations of all the buses of mentioned lines
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

print(len(sys.argv))

if not len(sys.argv) == 4:
    print('Invalid number of arguments. Run as: python show_bus_locations_um367.py <MTA key> <Busline>'
          )
    sys.exit()

# set key

key = sys.argv[1]

# set bus

bus = sys.argv[2]

fileName = sys.argv[3]

# generate url

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' \
    + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus

# get json data

response = urllib.urlopen(url)
data = response.read().decode('utf-8')
data = json.loads(data)

# fetch relvant data from nested json

rawBusData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'
        ][0]['VehicleActivity']

processedData = []

for busdata in rawBusData:
    journey = busdata['MonitoredVehicleJourney']
    rowDict = {}

    if len(journey['OnwardCalls']) < 1:
        rowDict['Latitude'] = journey['VehicleLocation']['Latitude']
        rowDict['Longitude'] = journey['VehicleLocation']['Longitude']
    else:

        onwardCall = journey['OnwardCalls']['OnwardCall']
        for calls in onwardCall:
            pdist = calls['Extensions']['Distances'
                    ]['PresentableDistance']
            sname = calls['StopPointName']
            if (pdist == 'approaching' or pdist == '1 stop away'):
                rowDict['Latitude'] = journey['VehicleLocation'
                        ]['Latitude']
                rowDict['Longitude'] = journey['VehicleLocation'
                        ]['Longitude']
                rowDict['Next Stop'] = sname
                rowDict['Stop Status'] = pdist
        if bool(rowDict):
            rowDict['Latitude'] = journey['VehicleLocation']['Latitude']
            rowDict['Longitude'] = journey['VehicleLocation'
                    ]['Longitude']
    processedData.append(rowDict)

dataFrame = pd.DataFrame(processedData)
dataFrame.to_csv(fileName, index=False)

