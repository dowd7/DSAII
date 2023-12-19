# Create a self-adjusting Hash Table that will store the 40 packages
class HashTable:

    # Initialize the Hash Table
    def __init__(self, size=40):
        self.list = [None] * size

    # Hash function to determine the index of the package
    def _get_hash(self, key):
        hash = 0

        # Generate a hash value based on the key
        for char in str(key):
            hash += ord(char)
        return hash % len(self.list)

    # Add a package to the hash table
    def insert(self, key, value):

        # Get the hash index
        hash = self._get_hash(key)
        keyValuePair = [key, value]

        # If the index is empty, add the package
        if self.list[hash] is None:
            self.list[hash] = list([keyValuePair])
            return True

        # If the index is not empty, check if the package is already in the index
        else:
            for pair in self.list[hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            # If the package is not in the index, add the package to the list
            self.list[hash].append(keyValuePair)
            return True

    # Get a package from the hash table
    def lookup(self, key):
        hash = self._get_hash(key)
        if self.list[hash] is not None:

            # iterate through the list to find the package
            for keyValuePair in self.list[hash]:
                if keyValuePair[0] == key:
                    return keyValuePair[1]
        return None

    # Remove a package from the hash table
    def remove(self, key):
        hash = self._get_hash(key)

        # If the index is empty, return false
        if self.list[hash] is None:
            return False

        # If the index is not empty, iterate through the list to find the package
        for i in range(0, len(self.list[hash])):
            if self.list[hash][i][0] == key:
                self.list[hash].pop(i)
                return True
        return False
