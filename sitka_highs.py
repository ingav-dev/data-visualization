import csv 
import matplotlib.pyplot as plt 
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# Get the dates, and high and low temperatures from this file.
	dates, highs, lows, pcrps = [], [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[5])
			low = int(row[6])
			pcrp = float(row[3])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
			pcrps.append(pcrp)

# Plot the highand low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_ylim([10, 150])
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#ax.plot(dates, pcrps, c='green', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures in Sitka - 2018", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
