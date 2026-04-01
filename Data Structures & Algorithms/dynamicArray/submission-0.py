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

        self.length += 1

        if self.length > self.capacity:

            self.resize()

        self.dynamic_array[self.length - 1] = n

    def popback(self) -> int:

        self.length -= 1
        return self.dynamic_array[self.length]

    def resize(self) -> None:

        self.dynamic_array.extend([0 for _ in range(self.capacity)])
        self.capacity *= 2

    def getSize(self) -> int:
        
        return self.length
    
    def getCapacity(self) -> int:

        return self.capacity