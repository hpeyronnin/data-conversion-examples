#read supeheroes.json
import json
from pprint import pprint
with open('superheroes.json') as f:
	data = json.load(f)

#create a blank list of powers
powers = []

members = data['members']

#loop over members
for member in members:
	member_powers = member['powers']
	for power in member_powers:
		#add taht to our list of powers
		powers.append(power)

#get a unique list of elements
unique_powers = list(set(powers))
#print those elements
pprint(unique_powers)

#Bobi and Henry participated in this 