# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced: bool = True
        
        def childrenBalanced(node: Optional[TreeNode]) -> int:

            nonlocal balanced

            if node:

                height: int = 1
                left_height: int = 0
                right_height: int = 0

                if node.left:

                    left_height = childrenBalanced(node.left)

                if node.right:

                    right_height = childrenBalanced(node.right)

                if abs(right_height - left_height) > 1:

                    balanced = False

                return height + max(left_height, right_height)

            else:

                return 0

        childrenBalanced(root)

        return balanced
