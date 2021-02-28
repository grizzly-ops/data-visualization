import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get high temperatures from this file.
	#highs = []
	# Get dates and high temperatures from this file.
	#dates, highs = [], []
	# Get dates, and high and low temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")	
		#high = int(row[5])
		#low = int(row[6])
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	print(highs)
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	print(header_row)
# Plot the high temperatures.
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#ax.plot(dates, highs, c='red')
#ax.plot(dates, lows, c='blue')
#ax.plot(highs, c='red')
# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.title("Daily high temperatures, July 2018", fontsize=24)
#plt.title("Daily high temperatures - 2018", fontsize=24)
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()