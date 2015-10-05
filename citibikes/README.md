PUI_Bycicle_Research
====================

research on Bicycle data for CUSP PUI 2015 class
Deadline: **Sunday, 10.4.2015**

authors = ['Maria Ortis', 
		   'Hannah Kates', 
		   'Xia Wang', 
		   'Michelle Ho',
		   'Philipp Kats']


### Our Hypothesis: riders in Brooklyn are younger than riders in Manhattan

- **Null hypothesis**: the average age of subscribers who start rides in Brooklyn stations is greater or the same as subscribers who start rides in Manhattan stations

- **Alternative hypothesis**: the average of subscribers who start rides in Brooklyn stations is lower than that of subscribers who start rides in Manhattan stations

## Data

- [**Rides data**](data/r_trips.csv)
- [**Stations data**](data/stations.csv)
- [**Boroughs borders**](data/borrows15_2.geojson)

#### Data sources
- [Citibike data](https://www.citibikenyc.com/system-data)
- [Borough boundaries](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm)

## Process

[General Notebook](3_Base Notebook_alt.ipynb)

We splitted the process into several parts

- [Trip Data preparation](2_Processing trips data.ipynb) [Maria Ortis', 'Hannah Kates', 'Michelle Ho', 'Philipp kats']
- [Borough classification](1_Stations_processing.ipynb) [Maria Ortis', 'Hannah Kates', 'Philipp Kats']
- [Age analysis](3_Base Notebook_alt.ipynb) [Maria Ortis', 'Hannah Kates']
- [t-Statistics](3_Base Notebook_alt.ipynb) ['Michelle Ho']
- [Mapping](citibikeuserage.jpg) ['Xia Wang']
- [Conclusion](3_Base Notebook_alt.ipynb) ['Michelle Ho']


