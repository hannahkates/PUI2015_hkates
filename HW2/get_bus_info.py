import urllib2
import json
import sys
import csv

## python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx M7 M7.csv
## api key: c167b534-49d9-414c-a182-6d9631b8ffe5

'''
ASSIGNMENT 2
'''

if __name__ == '__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	data = json.load(request)
	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	with open(sys.argv[3],'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])

		for b in buses:
			lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			long = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			if b['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'] == "":
				name = 'N/A'
			else: 
				name = b['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
			if b['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance'] == "":
				status = 'N/A'
			else:
				status = b['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
			row = [lat, long, name, status]
			writer.writerow(row)