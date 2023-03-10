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
        self.delivered_time = None
        self.departed_time = None

    def __str__(self):
        return f"ID: {self.id} | Address: {self.address} | City: {self.city} | Zip: {self.zip} | " \
               f"Deadline: {self.deadline} | Weight: {self.weight}"

    """
    Set the status for a package dependent upon time.
    
    -   If queried time is less than or equal to departed time, set to at hub
        If queried time is less than delivered time, set to en route
        Else set to delivered @ time
        
    Worst case: O(1)
    All operations are constant.
    :parameter queried_time: time constraint
    """
    def time_status(self, queried_time):
        if self.departed_time >= queried_time:
            return "At hub"
        elif self.delivered_time > queried_time:
            return "En route"
        else:
            return f"Delivered on time @ {self.delivered_time}"
