# Steven Dowd
# 011348256
# C950 - Data Structures and Algorithms II - Performance Assessment

import HashTable
import Package
import csv

h = HashTable.HashTable()

# Open the CSV file and read the data into the hash table
with open("csv/packages.csv") as packageFile:
    packageReader = csv.reader(packageFile, delimiter=',')

    # instantiate a package object for each row in the CSV file and insert it into the hash table
    for row in packageReader:
        package = Package.Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        h.insert(package.ID, package)

