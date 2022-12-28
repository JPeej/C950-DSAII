"""
Reference ZyBooks 7.8.2: Hash table with chaining
User created hash table with chaining for collision handling.
hash_package() : O(1)
insert()       : O(1)
lookup()       : O(n)
remove()       : O(n)
"""


class ChainHashTable:
    """
    Constructor for ChainHashTable class.
    Default value of initial table size is 10.
    Creates ten buckets. Chaining expected for practice.
    """

    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    """
    Hash package_id and return bucket correlating to calculated hash.
    Created to reduce code repetition.
    Worst case : O(1).
    :parameter package_id
    :return bucket within hash table
    """

    def hash_package(self, package_id):
        bucket = hash(package_id) % len(self.table)
        bucket_chain = self.table[bucket]
        return bucket_chain

    """
    Find queried package within hash table.
    Worst case : O(n)
    :parameter package_id
    :return queried package object if found
    :return None if not found
    """

    def lookup(self, package_id):
        bucket_chain = self.hash_package(package_id)
        for package in bucket_chain:
            if package[0] == package_id:
                return package
            else:
                return None

    """
    Insert new package into hash table.
    Appends to end of bucket list.
    Worst case : O(1).
    :parameter package_id
    :parameter package
    """

    def insert(self, package_id, package):
        bucket_chain = self.hash_package(package_id)
        bucket_chain.append(package)

    """
    Update package members with new values.
    Worst case : O(n)
    :parameter package_id
    :parameter package
    :return boolean on update
    """
    def update(self, package_id, package):
        queried_package = self.lookup(package_id)
        # If package exists, then update members.
        if queried_package is not None:
            queried_package[1] = package
            return True
        else:
            return False

    """
    Remove queried package from hash table.
    Worst case : O(n)
    :parameter package_id
    :parameter package
    :return boolean on removal
    """

    def remove(self, package_id):
        bucket_chain = self.hash_package(package_id)
        queried_package = self.lookup(package_id)
        if queried_package is not None:
            bucket_chain.remove(queried_package)
            return True
        else:
            return False
