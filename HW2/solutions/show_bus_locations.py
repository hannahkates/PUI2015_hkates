from __future__ import print_function
__author__ = 'fb55'

import sys
import urllib2
import json


if __name__ == '__main__':

    if not len(sys.argv) == 3:
        print ('''USAGE:
        $python show_bus_locations.py <MTA_KEY> <BUS_LINE>''')
        sys.exit()
    key = sys.argv[1]
    bus_line = sys.argv[2]
    print ('BUS LINE:', bus_line)

    this_url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + key + \
               '&VehicleMonitoringDetailLevel=calls&LineRef='+bus_line
#   print (this_url)
    response = urllib2.urlopen(this_url)
    data = json.load(response)
    nbusses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    print ('Number of Active Buses : %d' % nbusses)
    for i in range(nbusses):
        bi = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
            ['MonitoredVehicleJourney']['VehicleLocation']
#       print (bi)
        print ('Bus %d is at latitude %f and longitude %f' % (i, bi['Latitude'], bi['Longitude']))
