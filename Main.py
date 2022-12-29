import csv
from Truck import Truck
from ChainHashTable import ChainHashTable
from Package import Package
from datetime import timedelta

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
        limit = 2
        for location in distance_data:
            location_list = []
            for i in range(limit):
                try:
                    distance = float(location[i])
                    location_list.append(distance)
                except ValueError:
                    address = location[i].strip()
                    if '\n' in address:
                        find_escape = address.find('\n')
                        address = address[:find_escape]
                    addressTable.append(address)
                    pass
            limit += 1
            distanceTable.append(location_list)


def find_min_distance(truck):
    min_distance = 30  # Arbitrary large number
    current_location = truck.location
    current_index = addressTable.index(current_location)
    priority_package = None
    for i in range(len(truck.packages)):
        package_id = truck.packages[i]
        package_data = packageTable.search(package_id)
        package_data[1].status = "En route"
        package_address = package_data[1].address
        package_index = addressTable.index(package_address)
        try:
            distance = distanceTable[current_index][package_index]
        except IndexError:
            distance = distanceTable[package_index][current_index]
        if distance < min_distance:
            min_distance = distance
            priority_package = package_data[1]
    return priority_package, min_distance


def deliver_package(truck, package, distance):
    time_to = distance / truck.speed * 60
    truck.time = truck.time + timedelta(minutes=time_to)
    package.status = f"Delivered @ {truck.time}"
    truck.mileage += distance
    truck.location = package.address
    truck.packages.remove(package.id)


def return_to_hub(truck):
    current_location = truck.location
    current_index = addressTable.index(current_location)
    distance_to_hub = distanceTable[current_index][0]
    truck.mileage += distance_to_hub
    truck.location = "HUB"


def start_truck_route(truck):
    while len(truck.packages) > 0:
        package, distance = find_min_distance(truck)
        deliver_package(truck, package, distance)
    return_to_hub(truck)


load_package_data("Documentation/WGUPS Package File.csv")
load_distance_data("Documentation/WGUPS Distance Table.csv")

truck1 = Truck([1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 39], timedelta(hours=8, minutes=00))
truck2 = Truck([3, 4, 5, 6, 18, 25, 26, 36, 38, 40], timedelta(hours=9, minutes=5))
truck3 = Truck([2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 28, 32, 33, 35], timedelta(hours=10, minutes=20))

start_truck_route(truck1)
start_truck_route(truck2)
package_nine = packageTable.search(9)[1]
package_nine.address = "410 S State St"
start_truck_route(truck3)
total_mileage = truck1.mileage + truck2.mileage + truck3.mileage


class Main():
    print("Joshua Perry | 007217228")
    print("WGUPS Routing Performance Assessment")
    print(f"Total mileage: {total_mileage}\n")

    print("Please select one of the following options.")
    menu_input = input("1: Print all package info.\n"
                       "2: Print a single package info.\n"
                       "3: Print truck mileage.\n")
    if menu_input == 1:
        print("test")
        print(packageTable)
