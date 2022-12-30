"""
Reference ZyBooks 7.8.2: Hash table with chaining
Reference C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code
User created hash table with chaining for collision handling.
insert()       : O(1)
search()       : O(n)
remove()       : O(n)
"""


class ChainHashTable:

    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    """
    Insert package into hash table. 
    
    -   Calculate bucket on hash and length of table
        Append (id, package) into bucket
        
    Worst case: O(1)
    Appending to the end of a list is constant time and not dependent upon size of the list.
    :parameter package_id: value to hash
    :parameter package: package to insert
    """
    def insert(self, package_id, package):
        bucket = hash(package_id) % len(self.table)
        bucket_chain = self.table[bucket]
        package_kv = [package_id, package]
        bucket_chain.append(package_kv)

    """
    Search for a package in the hash table.
    
    -   Calculate bucket on hash and length of table
        For each package in bucket:
            If package in bucket:
                Return package:
            Else return None
        
    Worst case: O(n)
    The size of the bucket could scale to infinity and every value may have to be compared.
    :parameter package_id: id to search for
    :return package: package if found
    """
    def search(self, package_id):
        bucket = hash(package_id) % len(self.table)
        bucket_chain = self.table[bucket]
        for item in bucket_chain:
            if item[0] == package_id:
                return item
        return None

