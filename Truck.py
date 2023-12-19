class Truck:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.mileage = 0
        self.time = 0
        self.currentLocation = "HUB"
        self.currentPackage = None
        self.packagesDelivered = []
        self.packagesNotDelivered = []