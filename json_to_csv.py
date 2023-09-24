import json
import csv

with open('flight_data.csv', 'w', newline="") as file:
	writer=csv.writer(file)
	writer.writerow(['longitude', 'latitude', 'altitude'])
	# Open the JSON file
	with open('sample.json', 'r') as file2:
    	# Load JSON data into a Python data structure (e.g., a dictionary)
		data = json.load(file2)

	# Now you can work with the 'data' variable, which contains the JSON data
	for i in range(len(data['trace'])):
		print("longitude: ", data['trace'][i][1])
		print("latitude: ", data['trace'][i][2])
		print("altitude: ", data['trace'][i][0])
		writer.writerow([data['trace'][i][1], data['trace'][i][2], data['trace'][i][0]])
