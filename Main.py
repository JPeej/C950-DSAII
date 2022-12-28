import csv
from Truck import Truck
from ChainHashTable import ChainHashTable
from Package import Package
from datetime import time, timedelta

packageTable = ChainHashTable()
distanceTable = []
addressTable = []


def load_package_data(file_name):
    with open(file_name) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        package_data = list(package_data)
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            zipcode = package[4]
            deadline = package[5]
            weight = package[6]
            status = "Hub"
            new_package = Package(package_id, address, city, zipcode, deadline, weight, status)
            packageTable.insert_update(package_id, new_package)


def load_distance_data(file_name):
    with open(file_name) as distance_file:
        distance_data = csv.reader(distance_file, delimiter=',')
        next(distance_data)
        distance_data = list(distance_data)
        limit = 1
        for location in distance_data:
            location_list = []
            for i in range(limit):
                try:
                    distance = float(location[i])
                    location_list.append(distance)
                except ValueError:
                    address = location[i]
                    addressTable.append(address)
                    pass
            limit += 1
            distanceTable.append(location_list)


def deliver_package(truck):



load_package_data("Documentation/WGUPS Package File.csv")
load_distance_data("Documentation/WGUPS Distance Table.csv")

truck1 = Truck([1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 39], time(8, 00, 00, 00))
truck2 = Truck([3, 4, 5, 6, 18, 25, 26, 36, 37, 38, 40], time(9, 5, 00, 00))
truck3 = Truck([2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 28, 32, 33, 35], time(10, 20, 00, 00))
