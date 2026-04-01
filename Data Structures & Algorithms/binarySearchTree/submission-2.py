class Node:

    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
    
        self.root = None

    def insert(self, key: int, val: int) -> None:

        def helper(node, key, val) -> Node:

            if not node:

                return Node(key, val)

            if key < node.key:

                node.left = helper(node.left, key, val)

            elif key > node.key:

                node.right = helper(node.right, key, val)

            else: # BST doesn't allow duplicates: Replace mapping

                node.val = val

            return node

        self.root = helper(self.root, key, val)

    def get(self, key: int) -> int:

        def helper(node, key) -> int:

            if not node:

                return -1

            if node.key == key:

                return node.val
            
            elif key < node.key:

                return helper(node.left, key)

            else:

                return helper(node.right, key)

        return helper(self.root, key)

    def getMin(self, current: Node = None) -> int:

        if not current:

            current = self.root

        if not current:

            return -1

        while current.left:

            current = current.left

        return current.val

    def getMinNode(self, current: Node = None) -> Node:

        if not current:

            current = self.root

        if not current:

            return None

        while current.left:

            current = current.left

        return current

    def getMax(self) -> int:

        if not self.root:

            return -1

        current = self.root

        while current.right:

            current = current.right

        return current.val

    def remove(self, key: int) -> None:

        def helper(node: Node, key: int) -> Node:

            if not node:

                return None

            if key < node.key:

                node.left = helper(node.left, key)

            elif key > node.key:

                node.right = helper(node.right, key)

            else:

                if not node.left:

                    return node.right

                elif not node.right:

                    return node.left

                else: # Two Children

                    minimum = self.getMinNode(node.right)
                    node.key = minimum.key
                    node.val = minimum.val
                    node.right = helper(node.right, minimum.key) # Remove minimum of right side

            return node

        self.root = helper(self.root, key)

    def getInorderKeys(self) -> List[int]:

        # In-Order Traversal
        keys = []

        def inorder_traversal(node) -> None:

            if not node:

                return

            nonlocal keys

            # Left
            if node.left:

                inorder_traversal(node.left)

            # Self
            keys.append(node.key)

            # Right
            if node.right:

                inorder_traversal(node.right)

        inorder_traversal(self.root)

        return keys

