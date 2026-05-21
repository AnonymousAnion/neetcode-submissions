class Node:

    def __init__(self, total: int, l: Node = None, r: Node = None):

        self.sum = total
        self.left = None # Left Child Node
        self.right = None # Right Child Node
        self.min = l # The min index in the index range
        self.max = r # The max index in the index range

class SegmentTree:
    
    def __init__(self, nums: List[int]):

        self.root = SegmentTree.build(nums, 0, len(nums) - 1)

    @staticmethod
    def build(nums, l, r) -> SegmentTree:

        if l == r:

            return Node(nums[l], l, r)

        m = (l + r) // 2
        root = Node(0, l, r)
        root.left = SegmentTree.build(nums, l, m)
        root.right = SegmentTree.build(nums, m + 1, r)
        root.sum = root.left.sum + root.right.sum
        
        return root
    
    def update(self, index: int, val: int, current = None) -> None:

        if not current:

            current = self.root
        
        if current.min == current.max: # Leaf Node

            current.sum = val
            return

        m = (current.min + current.max) // 2

        # Note: Definitionally, all non-leaf nodes have 2 children.
        # This is because if their range is larger than one then there
        # exist two child nodes to define the halves of their range.
        if index > m:

            self.update(index, val, current.right)

        else:

            self.update(index, val, current.left)

        current.sum = current.left.sum + current.right.sum
    
    def query(self, L: int, R: int, current = None) -> int:

        if not current:

            current = self.root

        if L == current.min and R == current.max:

            return current.sum

        m = (current.min + current.max) // 2

        if L > m:

            return self.query(L, R, current.right)
        
        elif R <= m:

            return self.query(L, R, current.left)

        else:

            return (self.query(L, m, current.left) + 
                    self.query(m + 1, R, current.right))


