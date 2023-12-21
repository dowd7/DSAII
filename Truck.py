class Truck:
    def __init__(self, name, capacity=16):
        self.name = name
        self.capacity = capacity
        self.mileage = 0
        self.startTime = 0
        self.time = 0
        self.currentLocation = "4001 South 700 East"
        self.currentPackage = None
        self.packagesNotDelivered = []