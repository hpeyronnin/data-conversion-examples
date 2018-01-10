vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "cheese"},
 {"name": "chicken"}
]

print(vegetables)

import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'length'])
    for vegetable in vegetables:
    	#i want the name of hte vegetable
    	vegetable_name = vegetable['name']
    	#i want the length of that word
    	veggie_name_length = len(vegetable_name)
    	#write those to csv
    	writer.writerow([vegetable_name, veggie_name_length])