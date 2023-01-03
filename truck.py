SPEED = 18  # mph
CAPACITY = 16  # packages
INITIAL_MILEAGE = 0
INITIAL_LOCATION = "HUB"


"""
Truck class to hold and deliver packages.
"""
class Truck:

    def __init__(self, packages, initial_time):
        self.speed = SPEED
        self.capacity = CAPACITY
        self.mileage = INITIAL_MILEAGE
        self.location = INITIAL_LOCATION
        self.packages = packages
        self.delivered_time = initial_time
        self.departed_time = initial_time

    def __str__(self):
        return f"Mileage: {self.mileage} | Location: {self.location} | Packages: {self.packages}"
