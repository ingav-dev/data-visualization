import csv 

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data 
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	brights, lons, lats = [], [], []
	for row in reader: 
		brights.append(round(float(row[2])))
		lons.append(row[1])
		lats.append(row[0])

# Map the fires.
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'marker': {
		'size': [bright/25 for bright in brights],
		'color': brights,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Brightness'},
	},
}]

my_layout = Layout(title="World fires")

fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename='global_fires.html')