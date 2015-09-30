import urllib2
import json
import sys
import csv

## sample input: python show_bus_locations.py xxxx-xxxx-xxxx-xxxx-xxxx B52
## api key: c167b534-49d9-414c-a182-6d9631b8ffe5

'''
ASSIGNMENT 1
'''

if __name__ == '__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	data = json.load(request)
	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	print 'Bus Line : ', sys.argv[2]
	print 'Number of Active Buses : ', str(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))
	busnum = 0
	for b in buses:
		lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		long = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print 'Bus ', str(busnum), ' is at latitude', str(lat), ' and longitude', str(long)
		busnum += 1