# Steven Dowd
# 011348256
# C950 - Data Structures and Algorithms II - Performance Assessment

import HashTable
import Package
import csv
import Truck

h = HashTable.HashTable()

# Open the CSV file and read the data into the hash table
with open("csv/packages.csv") as packageFile:
    packageReader = csv.reader(packageFile, delimiter=',')

    # instantiate a package object for each row in the CSV file and insert it into the hash table
    for row in packageReader:
        package = Package.Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        h.insert(package.ID, package)

# Get the address data from the CSV file
with open("csv/addresses.csv") as addressFile:
    addressList = csv.reader(addressFile, delimiter=',')
    addressList = list(addressList)

# Get the distance data from the CSV file
with open("csv/distances.csv") as distanceFile:
    distanceList = csv.reader(distanceFile, delimiter=',')
    distanceList = list(distanceList)


def getAddressIndex(address):
    for row in addressList:
        if address in row[2]:
            return int(row[0])


def calculateDistance(addressIndex1, addressIndex2):
    # Get the distance between two addresses
    distance = distanceList[addressIndex1][addressIndex2]
    if distance == '':
        distance = distanceList[addressIndex2][addressIndex1]

    return distance


# Manually load the trucks
packages1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

packages2 = [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]

packages3 = [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]

truck1 = Truck.Truck()
truck2 = Truck.Truck()
truck3 = Truck.Truck()

# Load the trucks
for i in packages1:
    truck1.packagesNotDelivered.append(h.lookup(str(i)))

for i in packages2:
    truck2.packagesNotDelivered.append(h.lookup(str(i)))

for i in packages3:
    truck3.packagesNotDelivered.append(h.lookup(str(i)))


# Deliver the packages
# deliverPackages(truck1)
# deliverPackages(truck2)
# deliverPackages(truck3)


# loop 1-40 to print the package information
# for i in range(1, 41):
#     print(h.lookup(str(i)))


print(calculateDistance(0,2))