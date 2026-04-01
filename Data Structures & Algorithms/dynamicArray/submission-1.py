class DynamicArray:
    
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.dynamic_array = [0 for _ in range(capacity)]
        self.length = 0

    def get(self, i: int) -> int:

        if i < self.length:

            return self.dynamic_array[i]

        return -1

    def set(self, i: int, n: int) -> None:

        self.dynamic_array[i] = n

    def pushback(self, n: int) -> None:

        if self.length + 1 > self.capacity:

            self.resize()

        self.length += 1
        self.dynamic_array[self.length - 1] = n

    def popback(self) -> int:

        self.length -= 1
        return self.dynamic_array[self.length]

    def resize(self) -> None:

        self.capacity *= 2

        new_array = [0 for _ in range(self.capacity)]

        # Copy old values
        for i in range(0, self.length):

            new_array[i] = self.dynamic_array[i]

        self.dynamic_array = new_array

    def getSize(self) -> int:
        
        return self.length
    
    def getCapacity(self) -> int:

        return self.capacity