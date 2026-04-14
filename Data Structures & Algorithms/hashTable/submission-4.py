class HashTable:
    
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.array = []
        self.size = 0

        for i in range(self.capacity):

            self.array.append([])

    def insert(self, key: int, value: int) -> None:

        if self.array[key % self.capacity]:

            for i, l in enumerate(self.array[key % self.capacity]):

                k, val = l

                if k == key:

                    self.array[key % self.capacity][i] = (key, value)
                    return
            
        self.array[key % self.capacity].append((key, value))
        self.size += 1

        if self.size >= self.capacity / 2:

            self.resize()

    def get(self, key: int) -> int:

        if self.array[key % self.capacity]:

            for i, l in enumerate(self.array[key % self.capacity]):

                k, val = l

                if k == key:

                    return val

        return -1

    def remove(self, key: int) -> bool:

        if self.array[key % self.capacity]:

            for i, l in enumerate(self.array[key % self.capacity]):

                k, val = l

                if k == key:

                    self.array[key % self.capacity].pop(i)
                    self.size -= 1
                    return True

        return False

    def getSize(self) -> int:

        return self.size

    def getCapacity(self) -> int:

        return self.capacity

    def resize(self) -> None:

        new_array = []

        for i in range(self.capacity * 2):

            new_array.append([])

        for l in self.array:

            if l:

                i, val = l[0]
                new_array[i % (self.capacity * 2)] = [(i, val)]

        self.array = new_array
        self.capacity *= 2