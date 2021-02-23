
import os
import csv

output_file = '../documents/Github/python-challenge/pypoll/Resources/election_data.csv'

# REMEMBER TO DOUBLE CHECK WHICH ASSIGNMENT THIS IS BEFORE I CODE!
# Don't freak out, I can handle this. I can get this done. I can do this.

# Open and read csv
with open(output_file) as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
