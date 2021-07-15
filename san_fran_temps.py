import csv 
import matplotlib.pyplot as plt 
from datetime import datetime

filename = 'data/san_fran_2.csv'
index_max, index_min = 0, 0


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)
		if column_header == 'TMAX':
			index_max = index
		elif column_header == 'TMIN':
			index_min = index

	# Get the dates, and high and low temperatures from this file.
	dates, highs, lows, pcrps = [], [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[index_max])
			low = int(row[index_min])
			#pcrp = float(row[3])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
			#pcrps.append(pcrp)

# Plot the highand low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_ylim([10, 150])
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#ax.plot(dates, pcrps, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures in San Francisco - 2020", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
