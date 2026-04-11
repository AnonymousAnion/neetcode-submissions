class Node:

    def __init__(self, val = 0, next_node = None):

        self.val = val
        self.next = next_node

class MyCircularQueue:

    def __init__(self, k: int):

        self.head = None
        self.tail = None
        self.num_elements = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:

        if self.num_elements >= self.capacity:

            return False

        if not self.head:

            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head

        else:

            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.num_elements += 1
        return True

    def deQueue(self) -> bool:

        if self.isEmpty():

            return False

        if self.tail and self.tail == self.tail.next: # Only one element

            self.tail = None
            self.head = None
            self.num_elements -= 1
            return True

        self.tail.next = self.head.next
        self.head = self.tail.next

        if not self.head:

            self.tail = None

        self.num_elements -= 1
        return True

    def Front(self) -> int:
        
        if not self.head:

            return -1

        return self.head.val

    def Rear(self) -> int:
        
        if not self.tail:

            return -1

        return self.tail.val

    def isEmpty(self) -> bool:

        if not self.head:

            return True

        return False

    def isFull(self) -> bool:
        
        if self.num_elements == self.capacity:

            return True

        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()