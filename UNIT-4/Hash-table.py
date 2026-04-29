class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None
        

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (existing_key,_) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return True
        return False

ht = HashTable(5)
ht.insert("name", "Alice")
ht.insert("city", "New York")
ht.insert("course", "Data Structures")

# Search for keys
print("Name:", ht.search("name"))  # Output: Alice
print("City:", ht.search("city"))  # Output: New York

# Delete a key
print("Deleted 'city'?", ht.delete("city"))

#check again after deletion
print("City after deletion:", ht.search("city"))