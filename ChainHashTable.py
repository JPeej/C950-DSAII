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
    Hash package.id and return bucket correlating to calculated hash.
    Created to reduce code repetition.
    Worst case : O(1).
    :parameter package
    :return bucket within hash table
    """
    def hash_package(self, package):
        bucket = hash(package.package_id) % len(self.table)
        bucket = self.table[bucket]
        return bucket

    """
    Insert new package into hash table.
    Appends to end of bucket list.
    Worst case : O(1).
    :parameter package
    """
    def insert(self, package):
        bucket = self.hash_package(package)
        bucket.append(package)

    """
    Find queried package within hash table.
    Worst case : O(n)
    :parameter package
    :return queried package object if found
    :return None if not found
    """
    def lookup(self, package):
        bucket = self.hash_package(package)
        if package in bucket:
            return bucket[package]
        else:
            return None

    """
    Remove queried package from hash table.
    Worst case : O(n)
    :parameter package
    :return boolean on removal
    """
    def remove(self, package):
        bucket = self.hash_package(package)
        if package in bucket:
            bucket.remove(package)
            return True
        else:
            return False
