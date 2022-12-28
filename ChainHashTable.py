"""
Reference ZyBooks 7.8.2: Hash table with chaining
Reference C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code
User created hash table with chaining for collision handling.
hash_package() : O(1)
insert()       : O(1)
lookup()       : O(n)
remove()       : O(n)
update()       : O(n)
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

    def insert_update(self, package_id, package):
        bucket = hash(package_id) % len(self.table)
        bucket_chain = self.table[bucket]
        for item in bucket_chain:
            if item[0] == package_id:
                item[1] = package
        package_kv = [package_id, package]
        bucket_chain.append(package_kv)

    def search(self, package_id):
        bucket = hash(package_id) % len(self.table)
        bucket_chain = self.table[bucket]
        for item in bucket_chain:
            if item[0] == package_id:
                return item
        return None

    def remove(self, package_id):
        bucket = hash(package_id) % len(self.table)
        bucket_chain = self.table[bucket]
        for item in bucket_chain:
            if item[0] == package_id:
                bucket_chain.remove(item)
