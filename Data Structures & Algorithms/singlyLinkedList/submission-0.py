class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):

        self.head = Node(0)
        self.count = 0

    def __len__(self):

        return self.count
    
    def get(self, index: int) -> int:

        if index < 0 or index >= self.count:

            return -1

        current = self.head

        for i in range(index + 1):

            current = current.next

        return current.data

    def insertHead(self, val: int) -> None:
        
        new_node = Node(val)

        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1

    def insertTail(self, val: int) -> None:

        current = self.head

        while current.next:

            current = current.next

        current.next = Node(val)
        self.count += 1
        
    def remove(self, index: int) -> bool:

        if index < 0 or index >= self.count:

            return False

        current = self.head
        count = 0

        # Go to the node right before the node to be removed
        while current.next and count <= index - 1:

            current = current.next
            count += 1

        current.next = current.next.next # Get garbage collected!
        self.count -= 1
        return True

    def getValues(self) -> List[int]:
        
        values = []
        current = self.head

        while current.next:

            current = current.next
            values.append(current.data)

        return values
