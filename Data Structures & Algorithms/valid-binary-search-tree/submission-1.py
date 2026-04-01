# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isBST(node: Optional[TreeNode], min_val: int = -1001, max_val: int = 1001) -> bool:

            if not node:

                return True

            if node.val <= min_val or node.val >= max_val:

                return False

            left_max = min(max_val, node.val)
            right_min = max(min_val, node.val)

            return isBST(node.left, min_val, left_max) and isBST(node.right, right_min, max_val)

        return isBST(root)