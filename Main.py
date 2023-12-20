# Steven Dowd
# 011348256
# C950 - Data Structures and Algorithms II - Performance Assessment

import HashTable
import Package
import csv
import Truck
import datetime

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


def deliverPackages(truck):
    while len(truck.packagesNotDelivered) > 0:
        # Get the closest package
        closestPackage = truck.packagesNotDelivered[0]
        closestPackageIndex = 0
        closestDistance = 1000

        # Iterate through the packages to find the closest one
        for i in range(0, len(truck.packagesNotDelivered)):
            package = truck.packagesNotDelivered[i]
            addressIndex = getAddressIndex(package.address)

            # Get the distance between the current package and the truck's current location
            distance = calculateDistance(getAddressIndex(truck.currentLocation), addressIndex)

            # If the distance is less than the closest distance, update the closest package
            if float(distance) < float(closestDistance):
                closestPackage = package
                closestPackageIndex = i
                closestDistance = distance

        # Set the truck's current location to the closest package's address
        truck.currentLocation = closestPackage.address

        # Set the truck's current package to the closest package
        truck.currentPackage = closestPackage

        # Set the truck's mileage to the distance between the truck's current location and the closest package
        truck.mileage += float(closestDistance)

        # Set the truck's time to the distance between the truck's current location and the closest package
        truck.time += datetime.timedelta(hours=float(closestDistance) / 18)

        # Set the package's delivery time to the truck's time
        closestPackage.deliveryTime = truck.time

        # Add the package to the truck's delivered list and set the package's status to delivered
        truck.packagesDelivered.append(closestPackage)
        closestPackage.status = "Delivered"

        # Remove the package from the truck's not delivered list
        truck.packagesNotDelivered.pop(closestPackageIndex)


# Deliver the packages
truck1.time = datetime.timedelta(hours=8, minutes=30)
truck2.time = datetime.timedelta(hours=8, minutes=30)

deliverPackages(truck1)
deliverPackages(truck2)

truck3.time = min(truck1.time, truck2.time)
deliverPackages(truck3)


# loop 1-40 to print the package information
for i in range(1, 41):
    print(h.lookup(str(i)))


print(calculateDistance(0,2))
print(truck1.time)
print(truck1.mileage + truck2.mileage + truck3.mileage)
print(truck3.time)