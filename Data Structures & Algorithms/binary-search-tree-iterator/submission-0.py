# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.current = 0
        self.order = []

        current = root
        stack = []

        while current or stack:

            if current:

                 stack.append(current)
                 current = current.left

            else:

                current = stack.pop()
                self.order.append(current)
                current = current.right

    def next(self) -> int:
        
        val = self.order[self.current].val
        self.current += 1
        return val

    def hasNext(self) -> bool:
        
        return self.current < len(self.order)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()