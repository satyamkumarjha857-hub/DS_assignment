import hashlib

class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        # Generate multiple hash values
        return [int(hashlib.sha256((item+str(i)).encode()).hexdigest(), 16) % self.size
                for i in range(self.hash_count)]

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def __contains__(self, item):
        return all(self.bit_array[h] == 1 for h in self._hashes(item))


# Example usage
bf = BloomFilter(size=50, hash_count=3)
bf.add("apple")
bf.add("banana")

print("apple" in bf)   # True
print("banana" in bf)  # True
print("grape" in bf)   # False (or possibly True due to false positive)
