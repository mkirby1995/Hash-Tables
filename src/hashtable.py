# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # Check for capacity
        if len(list(filter(None, self.storage))) == self.capacity:
            #print(f"{len(list(filter(None, self.storage)))} == {self.capacity}
            #Resizing Storage")
            self.resize()

        # If not empty
        if self.storage[self._hash_mod(key)] != None:
            #print(f"{self._hash_mod(key)} already exists.")
            # Initialize current node
            current = self.storage[self._hash_mod(key)]
            while current != None:
            # If current key == key: overwrite value and break
                if current.key == key:
                    #print(f"Current node key(){current.key}) is the same as new key({key}). Overwriting Value")
                    current.value = value
                    break
                # Else see if current.next exists
                elif current.next == None:
                    #if not current.next =  LinkedPair(key, value)
                    #print(f"Reached End of List, Inserting key({key})")
                    current.next = LinkedPair(key, value)
                    break
                else:
                    #print(f"{current.key} {current.value}. No empty spot found. Moving to next node")
                    current = current.next
        # Else if empty
        else:
            #print(f"Inserting new node {key} {value} at {self._hash_mod(key)}")
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # if hash exists
        if self.storage[self._hash_mod(key)]:
            linked = self.storage[self._hash_mod(key)]
            if linked.key == key:
                self.storage[self._hash_mod(key)] = linked.next
                return
            while linked.next != None:
                if linked.next.key == key:
                    linked.next = linked.next.next
                    return
                linked = linked.next
            print("Warning")
        # Else return warning
        else:
            print("Warning!")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)]:
            linked = self.storage[self._hash_mod(key)]
            while linked.key != key and linked != None:
                linked = linked.next
            if linked.key == key:
                return linked.value
            else:
                return None
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        print(f"Doubling capacity from {self.capacity} to {self.capacity * 2}")
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in self.storage:
            if i != None:
                new_storage[self._hash_mod(i.key)] = LinkedPair(i.key, i.value)
                old_ll = i
                new_ll = new_storage[self._hash_mod(i.key)]
                while old_ll != None:
                    new_ll.next = old_ll.next
                    old_ll = old_ll.next
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
