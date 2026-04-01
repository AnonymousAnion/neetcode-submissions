class Node:

    def __init__(self, k: int = -1, v: int = -1):

        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        # Use Doubly Linked List
        self.head = Node()
        self.tail = self.head
        self.capacity = capacity
        self.node_map: Dict[int, Node] = {} # key, Node dict

    def debug(self) -> str:

        current = self.head
        nodes = [] 

        nodes.append("Length: " + str(len(self.node_map)))

        while current:

            if current == self.head:

                nodes.append("Head: " + str(current.val))

            elif current == self.tail:

                nodes.append("Tail: " + "({0}: {1})".format(current.key, current.val))

            else:

                nodes.append("Node: " + "({0}: {1})".format(current.key, current.val))

            current = current.next

        return ",".join(nodes)

    def insert_at_start(self, node: Node) -> None:

        # Breakup and insert the current node at the front
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        if node.next: node.next.prev = node

    def most_recently_used(self, node: Node) -> None:

        # Remove the node and Reconnect at its current position
        temp = node
        node.prev.next = node.next
        if node.next: node.next.prev = node.prev

        self.insert_at_start(node)

    def get(self, key: int) -> int:

        #print("Getting: ", key)

        # Always move accessed node to the head so that
        # it is the most recently used
        if key not in self.node_map:

            return -1

        current = self.node_map[key]

        # Special Case: if the current node is the tail,
        # then we need to move the tail to the previous
        # node when we're making the current node the
        # most recently used.
        if current == self.tail and len(self.node_map) > 1:

            self.tail = self.tail.prev

        self.most_recently_used(current)

        #print(self.debug())

        return current.val
        
    def put(self, key: int, value: int) -> None:

        #print("Putting: ({0}, {1})".format(key, value))

        # Check if key already present
        # Check if key already present
        if key in self.node_map:

            current = self.node_map[key]

            if self.tail == current and self.tail.prev != self.head:

                self.tail = self.tail.prev

            current.val = value
            self.most_recently_used(current)
            #print(self.debug())
            return

        new_node = Node(key, value)
        first_node: bool = False
        # Special Case: Need to set tail when initially populating cache
        if len(self.node_map) == 0:

            first_node = True

        self.node_map.update({key: new_node})

        # Always put node at the head so that
        # it is the most recently used
        self.insert_at_start(new_node)

        if first_node:

            self.tail = self.head.next

        # Pop off the tail of the doubly-linked list
        # to remove the least recently used
        if len(self.node_map) > self.capacity:

            del self.node_map[self.tail.key] # Remove map entry
            self.tail = self.tail.prev
            self.tail.next = None

        #print(self.debug())

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)