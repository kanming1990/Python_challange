import csv
f = open('cereal.csv')
csv_f = csv.reader(f)
for row in csv_f:
        print(row)