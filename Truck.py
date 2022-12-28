SPEED = 18  # mph
CAPACITY = 16  # packages
INITIAL_MILEAGE = 0
INITIAL_LOCATION = "4001 South 700 East"
INITIAL_LOAD = 0


class Truck:

    def __init__(self, packages, time):
        self.speed = SPEED
        self.capacity = CAPACITY
        self.mileage = INITIAL_MILEAGE
        self.location = INITIAL_LOCATION
        self.load = INITIAL_LOAD
        self.packages = packages
        self.time = time

    def __str__(self):
        return f"Mileage: {self.mileage} | Location: {self.location} | Packages: {self.packages} | Load: {self.load}"
