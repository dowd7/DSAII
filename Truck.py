class Truck:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.mileage = 0
        self.time = 0
        self.currentLocation = "4001 South 700 East"
        self.currentPackage = None
        self.packagesNotDelivered = []