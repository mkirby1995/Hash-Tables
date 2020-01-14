class Dynamic_array:


    def __init__(self, capacity = 8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity


    def insert(self, index, value):
        if self.count == self.capacity:
            self.resize()

        # Shift everything to the right
        for i in range(self.count, index):
            self.storage[i] = self.storage[i - 1]

        # Insert our value
        self.storage[index] = value
        self.count += 1


    def append(self, value):
        self.insert(self.count, value)
        self.count += 1


    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


    def replace(self, index, value):
        self.storage[index] = value


    def add_to_front(self, value):
        self.storage = [value] + self.storage
        self.count += 1


    def slice(self, begining_index, end_index):
        values_at_index = []

        for i in self.storage[begining_index:end_index]:
            values_at_index.append(i)

        return values_at_index


    def delete(self, index):
        self.replace(index, None)
