#Write a program that reads data from a CSV file and prints it to the console.
import csv
filename = 'C:/Users/Admin/Downloads/greenhouse.csv'
data = []
with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        data.append(row)
for row in data:
    print(row)
