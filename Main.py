import csv
from ChainHashTable import ChainHashTable
from Package import Package

packageTable = ChainHashTable()


def load_package_data(file_name, ):
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


load_package_data("Documentation/WGUPS Package File.csv")

for i in range(40):
    print(packageTable.search(i))