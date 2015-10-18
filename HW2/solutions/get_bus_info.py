from __future__ import print_function
__author__ = 'fb55'
import sys
import urllib2
import json


if __name__ == '__main__':
    if not len(sys.argv) == 4:
        print ('''USAGE:
        $python get_bus_line.py <MTA_KEY> <BUS_LINE>''')
        sys.exit()
    key,  bus_line, outfile = sys.argv[1:]
    of = open(outfile, 'w')
#   print ('#BUS LINE:', bus_line)
    print ('Latitude,Longitude,Stop Name,Stop Status', file=of)
    this_url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + key + \
               '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
#   print (this_url)
    response = urllib2.urlopen(this_url)
    data = json.load(response)
    nbusses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
#   ['MonitoredVehicleJourney'])
#   print ('Number of Active Buses : %d'%nbusses)
    for i in range(nbusses):
        biloc = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\
            [i]['MonitoredVehicleJourney']['VehicleLocation']
        next_stop = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\
            [i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
#       print (next_stop)
#       print ('Bus %d is at latitude %f and longitude %f'%(i,biloc['Latitude'], biloc['Longitude']))
        print ("%f,%f," % (biloc['Latitude'], biloc['Longitude']), end='', file=of)
        if len(next_stop) < 1:
            print ('N/A', 'N/A', file=of)
        else:
            print ("%s,%s" % (next_stop[0]['StopPointName'],
                              next_stop[0]['Extensions']['Distances']['PresentableDistance']),
                   file=of)
