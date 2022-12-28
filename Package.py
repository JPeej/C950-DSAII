"""
Class for creating package objects.
Members are public access by default and don't need setters/getters.
Further implementation and enterprise use would encourage private access.
"""


class Package:

    def __init__(self, package_id, address, city, zipcode, deadline, weight, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.zip = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
