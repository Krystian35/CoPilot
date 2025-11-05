import csv
import json
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define input and output file paths
csv_file = os.path.join(current_dir, 'data.csv')
json_file = os.path.join(current_dir, 'data.json')

# Read CSV and convert to JSON
with open(csv_file, 'r') as csvfile:
    # Read CSV using DictReader
    csv_data = list(csv.DictReader(csvfile))

# Write JSON
with open(json_file, 'w') as jsonfile:
    json.dump(csv_data, jsonfile, indent=2)