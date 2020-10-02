class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.number_of_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load_factor = self.number_of_items / self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        value_found = False # flag to check wether or not the value was found in the linked list
        index = self.hash_index(key)
        if self.storage[index] is not None:
            curr_node = self.storage[index]
            while curr_node is not None:
                if curr_node.key == key:
                    curr_node.value = value
                    value_found = True
                curr_node = curr_node.next
            if value_found == False:
                new_entry = HashTableEntry(key, value) # create a new entry
                curr_head = self.storage[index] # get the current head
                new_entry.next = curr_head # make the pointer of the new entry point to the current head
                self.storage[index] = new_entry # make the new entry the new head
                self.number_of_items += 1 # Update number of items in the hash_table
        else:
            self.storage[index] = HashTableEntry(key, value)
            self.number_of_items += 1 # Update number of items in the hash_table
        # check load factor
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        key_found = False
        index = self.hash_index(key)
        prev = None
        curr_node = self.storage[index]
        while curr_node is not None:
            if curr_node.key == key:
                if prev is None: # if the node to delete is the head
                    self.storage[index] = curr_node.next
                else:
                    prev.next = curr_node.next
                key_found = True
                self.number_of_items -= 1 # Update number of items in the hash_table
            prev = curr_node
            curr_node = curr_node.next
        if key_found == False:
            print("Warning: Key not found.")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        curr_node = self.storage[index]
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_number_of_items = 0
        prev_storage = self.storage
        new_storage = [None] * new_capacity
        for prev_item in prev_storage:
            if prev_item is not None: 
                if prev_item.next is not None:
                    while prev_item is not None:
                        if new_storage[self.hash_index(prev_item.key)] is not None:
                            new_entry = HashTableEntry(prev_item.key, prev_item.value)
                            curr_head = new_storage[self.hash_index(prev_item.key)]
                            new_entry.next = curr_head
                            new_storage[self.hash_index(prev_item.key)] = new_entry
                            new_number_of_items += 1
                        else:
                            new_storage[self.hash_index(prev_item.key)] = HashTableEntry(prev_item.key, prev_item.value)
                            new_number_of_items += 1
                        prev_item = prev_item.next
                else:
                    if new_storage[self.hash_index(prev_item.key)] is not None:
                        new_entry = HashTableEntry(prev_item.key, prev_item.value)
                        curr_head = new_storage[self.hash_index(prev_item.key)]
                        new_entry.next = curr_head
                        new_storage[self.hash_index(prev_item.key)] = new_entry
                        new_number_of_items += 1
                    else:
                        new_storage[self.hash_index(prev_item.key)] = HashTableEntry(prev_item.key, prev_item.value)
                        new_number_of_items += 1
        self.storage = new_storage
        self.number_of_items = new_number_of_items


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
