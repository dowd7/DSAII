# Steven Dowd
# 011348256
# C950 - Data Structures and Algorithms II - Performance Assessment

import HashTable
import Package
import csv
import Truck
import datetime

# instantiate a hash table
h = HashTable.HashTable()

# Open the CSV file and read the data into the hash table
with open("csv/packages.csv") as packageFile:
    packageReader = csv.reader(packageFile, delimiter=',')

    # instantiate a package object for each row in the CSV file and insert it into the hash table
    # O(n) time complexity
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


# return the index of the address in the address list, which can be used to get the distance between two addresses
def getAddressIndex(address):
    for row in addressList:
        if address in row[2]:
            return int(row[0])


# return the distance between two address indexes
def calculateDistance(addressIndex1, addressIndex2):
    # Get the distance between two addresses
    distance = distanceList[addressIndex1][addressIndex2]

    # If the distance is blank, get the distance between the addresses in reverse order
    if distance == '':
        distance = distanceList[addressIndex2][addressIndex1]

    return distance


# Manually determine the packages for each truck
packages1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

packages2 = [2, 3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]

packages3 = [4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33]

# instantiate the trucks
truck1 = Truck.Truck("Truck 1")
truck2 = Truck.Truck("Truck 2")
truck3 = Truck.Truck("Truck 3")

# Load the trucks
for i in packages1:
    truck1.packagesNotDelivered.append(h.lookup(str(i)))

for i in packages2:
    truck2.packagesNotDelivered.append(h.lookup(str(i)))

for i in packages3:
    truck3.packagesNotDelivered.append(h.lookup(str(i)))


# Deliver the packages for a given truck, uses the nearest neighbor algorithm
# O(n^2) time complexity
def deliverPackages(truck):
    # Truck's current time is set to the truck's start time
    truck.time = truck.startTime

    # Loops until all packages have been delivered
    while len(truck.packagesNotDelivered) > 0:
        # Get the closest package
        closestPackage = truck.packagesNotDelivered[0]
        closestPackageIndex = 0
        closestDistance = 999

        # Iterate through the packages to find the closest one
        # O(n) time complexity
        for i in range(0, len(truck.packagesNotDelivered)):
            package = truck.packagesNotDelivered[i]

            # Set the package's status to en route on the truck
            package.status = "En Route on " + truck.name + " as of " + str(truck.startTime)
            addressIndex = getAddressIndex(package.address)
            package.truck = truck

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

        # Remove the package from the truck's not delivered list
        truck.packagesNotDelivered.pop(closestPackageIndex)

    # when out of packages, send the truck back to the hub
    truck.currentLocation = "4001 South 700 East"
    truck.mileage += float(calculateDistance(getAddressIndex(truck.currentPackage.address)
                                             , getAddressIndex(truck.currentLocation)))
    truck.time += datetime.timedelta(hours=float(calculateDistance(getAddressIndex(truck.currentPackage.address)
                                                                   , getAddressIndex(truck.currentLocation))) / 18)


# Deliver the packages
truck1.startTime = datetime.timedelta(hours=8, minutes=00)
truck2.startTime = datetime.timedelta(hours=9, minutes=15)

deliverPackages(truck1)
deliverPackages(truck2)

# Truck 3 can't leave until truck 1 or truck 2 return
truck3.startTime = min(truck1.time, truck2.time)
deliverPackages(truck3)


# Verify the package's address and status at a given time
def verifyPackage(time, package):
    # fix the address for package 9
    if package.ID == "9" and time >= datetime.timedelta(hours=10, minutes=20):
        package.address = "410 S State St"
        package.zip = "84111"

    # if the entered time is before the package's start time, set the status to at the hub
    # if the package has been delivered before the entered time, set the status to delivered
    if time < package.truck.startTime:
        package.status = "At the Hub"
    if package.deliveryTime <= time:
        package.status = "Delivered at " + str(package.deliveryTime) + " by " + package.truck.name


# User can enter a time in the format HH:MM to see the status of all packages at that time
class Main:
    print("The total mileage for all trucks is: " + str(truck1.mileage + truck2.mileage + truck3.mileage) + " miles.")

    # The User will be prompted to enter a time in the format HH:MM to see the status of all packages at that time
    time = input("Enter a time in the format HH:MM to see the status of all packages at that time: ")
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])
    time = datetime.timedelta(hours=hour, minutes=minute)

    # ask if the user wants to see all packages or one specific package
    allPackages = input("Would you like to see the status of all packages or 1 specific package? (All/1): ")

    if allPackages == "1":
        packageID = input("Enter the package ID: ")
        package = h.lookup(packageID)
        verifyPackage(time, package)
        print("The status of package " + packageID + " at " + str(time) + " is: ")
        print(package)
        exit()

    if allPackages == "All" or allPackages == "all":
        print("The status of all packages at " + str(time) + " is: ")

        # iterate through the hash table, verify and print the package
        # O(n) time complexity
        for i in range(1, 41):
            package = h.lookup(str(i))
            verifyPackage(time, package)
            print(package)
        exit()
