#read superhero.json into a variable
import json
from pprint import pprint
with open('superheroes.json') as f:
	data = json.load(f)
#select members
members = data['members']
#write header to csv
import csv

with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header = [
		'name', 
		'age', 
		'secretIdentity', 
		'powers', 
		'squadName', 
		'homeTown', 
		'formed', 
		'secretBase', 
		'active']
	writer.writerow(header)

	#loop over the members
	for m in members:
		#Fore each member, get hte row
		row = [
			m['name'],
			m['age'],
			m['secretIdentity'],
			str(m['powers']),
			data['squadName'],
			data['homeTown'],
			data['formed'],
			data['secretBase'],
			data['active']
		]
		writer.writerow(row)

#save output to csv file

