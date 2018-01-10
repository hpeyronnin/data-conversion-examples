#read vegetables.csv
import csv
import json

with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)


with open('vegetables.json', 'w') as f:
	json.dump(rows, f, indent=2)