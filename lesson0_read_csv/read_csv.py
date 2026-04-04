# csv library  for interact with csv file
import csv

# Read csv file
with open('read_csv/person_data.csv', 'r') as file:
    # to read data in csv file, using DictReader()
    person_data = csv.DictReader(file)
    print(person_data.fieldnames)
    for data in person_data:
        print(data)
        print(f'{data['id']} - {data['name']} - {data['age']} - {data['hometown']}')

# Append new data in csv file
with open('read_csv/person_data.csv', 'a', newline='') as file:
    # give column names to the writer.
    # use  DictWriter() to write or append.
    fieldNames = ['id','name','age','hometown']
    writer = csv.DictWriter(file,fieldnames=fieldNames)
    writer.writerow({'id': 3, 'name': 'Yi', 'age':'32', 'hometown':'Ilonia'})
    # Note: newline='' is added to prevent Python from adding extra blank lines on Windows.

# Delete a row
rows_to_keep = []
fieldNames = []

with open('read_csv/person_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    fieldNames = reader.fieldnames
    for row in reader:
        if row[fieldNames[0]] != '1':
            rows_to_keep.append(row)

with open('read_csv/person_data.csv', 'w', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(rows_to_keep)
