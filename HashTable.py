# Create a self-adjusting Hash Table that will store the 40 packages
class HashTable:

    # Initialize the Hash Table
    def __init__(self, size=40):
        self.map = [None] * size

    # Hash function to determine the index of the package
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % len(self.map)

    # Add a package to the hash table
    def insert(self, key, value):
        hash = self._get_hash(key)
        keyValue = [key, value]

        if self.map[hash] is None:
            self.map[hash] = list([keyValue])
            return True
        else:
            for pair in self.map[hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[hash].append(keyValue)
            return True

    # Get a package from the hash table
    def get(self, key):
        hash = self._get_hash(key)
        if self.map[hash] is not None:
            for keyValuePair in self.map[hash]:
                if keyValuePair[0] == key:
                    return keyValuePair[1]
        return None

    # Delete a package from the hash table
    def delete(self, key):
        hash = self._get_hash(key)

        if self.map[hash] is None:
            return False
        for i in range(0, len(self.map[hash])):
            if self.map[hash][i][0] == key:
                self.map[hash].pop(i)
                return True

