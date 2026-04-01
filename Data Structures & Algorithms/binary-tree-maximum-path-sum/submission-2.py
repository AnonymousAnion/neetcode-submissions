# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maximum = -1001
        
        def helper(root: Optional[TreeNode]) -> int:

            nonlocal maximum

            if not root:

                return -1001

            leftMax = helper(root.left)
            rightMax = helper(root.right)

            maximum = max(maximum, leftMax, rightMax, root.val, leftMax + rightMax + root.val, leftMax + root.val, rightMax + root.val)

            return max(root.val, leftMax + root.val, rightMax + root.val)

        helper(root)

        return maximum