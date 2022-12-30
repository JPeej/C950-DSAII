"""
Joshua Perry 007217228
Screenshots are found in the Documentation directory.
Referenced C950 WGUPS Project Implementation Steps - Example
"""

import csv
from Truck import Truck
from ChainHashTable import ChainHashTable
from Package import Package
from datetime import timedelta

packageTable = ChainHashTable()
distanceTable = []
addressTable = []
all_packages = []

"""
Take a given CSV file containing package information and insert it into a hash table.

-   Open file and read with ',' delimiter
        Convert to list
        For each package in list:
            Parse through package and save to respective member
            Create new package with parsed data
            Insert new package into hash table
            
Worst case: O(n)
The amount of packages within the CSV file can grow up to infinity.
As this function must parse each package, the function must scale with the size of the function in a linear fashion.
:parameter file_name: name of CSV file
"""

def load_package_data(file_name):
    with open(file_name) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        package_data = list(package_data)
        for package in package_data:  # Worst case: O(n)
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            zipcode = package[4]
            deadline = package[5]
            weight = package[6]
            status = "Hub"
            new_package = Package(package_id, address, city, zipcode, deadline, weight, status)
            packageTable.insert(package_id, new_package)


"""
Take a given CSV file containing package information and insert it into a list

-   Open file and read with ',' delimiter
    Ignore column label row
    Convert to list
    Set read limit.
    For each location in distance list:
        Create list for location
        For each column up to limit:
            try:
                Append distance to location list
            except query is address:
                Format address
                Append address to address list
        Increment limit
        Append location list to distance list
        
Worst case: O(n^2)
Although only half on the table is read, the rows and/or columns may grow to infinity.
Each row and column must be read. Implemented with nested for loops. Therefore, n^2.
:parameter file_name: name of CSV file
"""

def load_distance_data(file_name):
    with open(file_name) as distance_file:
        distance_data = csv.reader(distance_file, delimiter=',')
        next(distance_data)
        distance_data = list(distance_data)
        limit = 2  # Only half of table needs to be read as distance is either in (x,y) or (y,x)
        for location in distance_data:  # Worst case: O(n)
            location_list = []
            for i in range(limit):  # Worst case: O(n)
                try:
                    distance = float(location[i])
                    location_list.append(distance)
                except ValueError:  # If queried (x,y) in table is the address
                    address = location[i].strip()
                    if '\n' in address:  # Format read list to similar format found in package address
                        find_escape = address.find('\n')
                        address = address[:find_escape]
                    addressTable.append(address)
                    pass
            limit += 1
            distanceTable.append(location_list)


"""
Nearest neighbor algorithm.
Heuristically find the shortest delivery path for all packages on the truck by going to the closest package from 
the current location.

-   Set an arbitrarily large number to min_distance
    Get current truck location
    Get index of current location within address table
    Set priority_package to None
    For all packages in the truck:
        Get package id
        Get the package data
        Set package status to En route
        Get the package address
        Get index of package address within address table
        Find distance value with either (package, current) or (current, package)
        If distance value is less than min_distance:
            Set min_distance to distance value
            Set package as priority_package
    Return priority_package and min_distance
    
Worst case: O(n)
Looping through the packages in the truck is constant time. Big O notation gives an upper bound to another function
in concern with it's end behavior. As the max amount of packages in a truck is 16, the end behavior for looping through
n packages within a truck is a constant 16. This can be upper bound by a constant, c = 17, multiplied by 1. Therefore,
O(1). 
Searching through all packages within the package table is O(n) as the table can scale to infinity.
:parameter truck: delivery truck to route
:return priority_package: next package to deliver
:return min_distance: distance to travel for next package 
"""

def find_min_distance(truck):
    min_distance = 30  # Arbitrary large number
    current_location = truck.location
    current_index = addressTable.index(current_location)
    priority_package = None
    for i in range(len(truck.packages)):  # Worst case: O(1) see above comment
        package_id = truck.packages[i]
        package_data = packageTable.lookup(package_id)  # Worst case O(n)
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


"""
Process to deliver package once at location.

-   Calculate time to travel and increment it to tracked time
    Set package departed and delivered time
    Increment truck mileage
    Set truck current location
    Remove package from truck
    Remove package from package table
    
Worst case: O(1)
Looping through the the packages in the truck is constant time. Big O notation gives an upper bound to another function
in concern with it's end behavior. As the max amount of packages in a truck is 16, the end behavior for looping through
n packages within a truck is a constant 16. This can be upper bound by a constant, c = 17, multiplied by 1. Therefore,
O(1). 
:parameter truck: truck on route
:parameter package: package to deliver
:parameter distance: distance traveled to address
"""

def delivery(truck, package, distance):
    time_to = distance / truck.speed * 60
    truck.delivered_time = truck.delivered_time + timedelta(minutes=time_to)
    package.status = f"Delivered @ {truck.delivered_time}"
    package.departed_time = truck.departed_time
    package.delivered_time = truck.delivered_time
    truck.mileage += distance
    truck.location = package.address
    truck.packages.remove(package.id)  # Worst case: O(1) see above comment


"""
Calculate mileage to return truck to the hub.

-   Get truck current location
    Get index of current location in address table
    Get distance to hub from distance table
    Increment mileage
    Set truck location to hub
    
Worst case: O(1)
All operations are constant time.
:parameter truck: truck on route
"""

def return_to_hub(truck):
    current_location = truck.location
    current_index = addressTable.index(current_location)
    distance_to_hub = distanceTable[current_index][0]
    truck.mileage += distance_to_hub
    truck.location = "HUB"


"""
Start delivering packages for a truck.

-   While packages are on the truck:
        Find nearest package to deliver
        Deliver package
    Truck back to hub
    
Worst case: O(n)
Looping through the the packages in the truck is constant time. Big O notation gives an upper bound to another function
in concern with it's end behavior. As the max amount of packages in a truck is 16, the end behavior for looping through
n packages within a truck is a constant 16. This can be upper bound by a constant, c = 17, multiplied by 1. Therefore,
O(1). 
The two methods within the while loop have been analyzed above.
:parameter truck: truck on route
"""

def start_truck_route(truck):
    while len(truck.packages) > 0:  # Worst case: O(1) see above comment
        package, distance = find_min_distance(truck)  # Worst case: O(n)
        delivery(truck, package, distance)  # Worst case: O(1)
    return_to_hub(truck) # Worst case: O(1)


"""
The provided methods and packages are now used to calculate an approximation for shortest delivery mileage.
Package, distance, and address data are loaded into their respective data structures.
Three truck objects are created and packages are loaded manually. 
Each truck in turn runs the self adjusting algorithm, start_truck_route, where it's total mileage is ultimately found.
Before truck3 departs, package 9 has it's address updated.
Finally, a total mileage across all three trucks is calculated. 
Worst case: O(n^2)
"""

load_package_data("Documentation/WGUPS Package File.csv")  # Worst case: O(n)
load_distance_data("Documentation/WGUPS Distance Table.csv")  # Worst case: O(n^2)

# Heuristically and manually added packages to each truck.
truck1 = Truck([1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 39], timedelta(hours=8, minutes=00))
truck2 = Truck([3, 4, 5, 6, 18, 25, 26, 36, 38, 40], timedelta(hours=9, minutes=5))
truck3 = Truck([2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 28, 32, 33, 35], timedelta(hours=10, minutes=21))

start_truck_route(truck1)  # Worst case: O(n)
start_truck_route(truck2)  # Worst case: O(n)

# Truck 3 doesn't leave until 10:20.
# Package 9 isn't updated until 10:20.
# Therefore, package updating before truck leaves is applicable.
package_nine = packageTable.lookup(9)[1]  # Worst case: O(n)
package_nine.address = "410 S State St"
start_truck_route(truck3)  # Worst case: O(n)

total_mileage = truck1.mileage + truck2.mileage + truck3.mileage

"""
Start CLI to interact with data.
Worst case: O(n)
    As only one operation can be done at a time
"""

class Main:
    program_running = True
    print("Joshua Perry | 007217228")
    print("WGUPS Routing Performance Assessment")
    print(f"Total mileage: {total_mileage}")

    # Main menu options
    while program_running:
        print("\nPlease select one of the following options.")
        menu_input = int(input("1: Print all package info.\n"
                               "2: Print a single package info.\n"
                               "3: Print truck mileage.\n"
                               "4: Exit\n"
                               "Enter: "))

        # All package menu options
        if menu_input == 1:
            all_input = int(input("\n1: End of day.\n"
                                  "2: With time constraint.\n"
                                  "Enter: "))
            # Print all packages after delivery
            if all_input == 1:
                eod = timedelta(hours=24)
                for i in range(1, 41):
                    package = packageTable.lookup(i)[1]  # Worst case: O(n)
                    status = package.time_status(eod)
                    print(f"{package} | Status: {status}")
            # Print all packages with a time constraint
            else:
                print("\nPlease define a time in which package info will be constrained to.")
                hour = int(input("Enter an hour (24 hour clock): "))
                min = int(input("Enter a minute: "))
                queried_time = timedelta(hours=hour, minutes=min)
                for i in range(1, 41):
                    package = packageTable.lookup(i)[1]  # Worst case: O(n)
                    status = package.time_status(queried_time)
                    print(f"{package} | Status: {status}")

        # Single package menu options
        elif menu_input == 2:
            package_id = int(input("\nEnter the ID of the package you wish to query: "))
            single_input = int(input("1: End of day.\n"
                                     "2: With time constraint.\n"
                                     "Enter: "))
            package = packageTable.lookup(package_id)[1]  # Worst case: O(n)
            # Print single package after delivery
            if single_input == 1:
                eod = timedelta(hours=24)
                status = package.time_status(eod)
                print(f"{package} | Status: {status}")
            # Print single package with time constraint
            else:
                print("\nPlease define a time in which package info will be constrained to.")
                hour = int(input("Enter an hour (24 hour clock): "))
                min = int(input("Enter a minute: "))
                queried_time = timedelta(hours=hour, minutes=min)
                status = package.time_status(queried_time)
                print(f"{package} | Status: {status}")

        # Truck mileage display
        elif menu_input == 3:
            print(f"\nTruck 1: {truck1.mileage}")
            print(f"Truck 2: {truck2.mileage}")
            print(f"Truck 3: {truck3.mileage}")
            print(f"Total mileage: {total_mileage}")

        # Quit
        elif menu_input == 4:
            program_running = False
