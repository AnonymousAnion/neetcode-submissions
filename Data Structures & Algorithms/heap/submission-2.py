class MinHeap:
    
    def __init__(self):

        self.min_heap = []

    def swap(self, i1: int, i2: int) -> None:

        tmp = self.min_heap[i1]
        self.min_heap[i1] = self.min_heap[i2]
        self.min_heap[i2] = tmp

    def push(self, val: int) -> None:

        self.min_heap.append(val)
        index = len(self.min_heap) - 1
        parent = (index - 1) // 2

        while index > 0 and self.min_heap[parent] > self.min_heap[index]:

            # Swap parent and child
            self.swap(index, parent)

            # Reassign index and parent
            index = parent
            parent = (index - 1) // 2

    def pop(self) -> int:
        
        if self.is_empty():

            return -1

        # Swap first and last element and pop the last element
        min_val: int = self.min_heap[0]
        self.min_heap[0] = self.min_heap[-1]
        self.min_heap.pop()

        # Re-establish the heap property
        i = 0
        left = 2 * i + 1
        right = 2 * i + 2

        while left < len(self.min_heap): # while the current node has children

            if (right < len(self.min_heap) and 
            self.min_heap[right] < self.min_heap[left] and
            self.min_heap[i] > self.min_heap[right]):

                # Swap right child
                self.swap(i, right)
                i = right

            elif self.min_heap[i] > self.min_heap[left]:

                # Swap left child
                self.swap(i, left)
                i = left

            else:
                break

            left = 2 * i + 1
            right = 2 * i + 2

        return min_val

    def is_empty(self) -> bool:

        return len(self.min_heap) <= 0

    def top(self) -> int:
        
        if self.is_empty():

            return -1

        return self.min_heap[0]

    def heapify(self, nums: List[int]):
        
        self.min_heap = nums
        cur = (len(self.min_heap) - 1) // 2

        while cur >= 0:

            i = cur
            left = 2 * i + 1
            right = 2 * i + 2

            # print("i: ", i)
            # print("left: ", left)
            # print("right: ", right)

            # Percolate down
            while left < len(self.min_heap):

                if (right < len(self.min_heap) and
                self.min_heap[right] < self.min_heap[left] and
                self.min_heap[i] > self.min_heap[right]):

                    # Swap right child
                    self.swap(i, right)
                    i = right

                elif self.min_heap[i] > self.min_heap[left]:

                    # Swap left child
                    self.swap(i, left)
                    i = left

                else:

                    break

                left = 2 * i + 1
                right = 2 * i + 2

            cur -= 1