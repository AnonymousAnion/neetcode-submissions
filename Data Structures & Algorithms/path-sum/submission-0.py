# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:

            return False

        # Leaf with remaining value
        if not root.left and not root.right and root.val == targetSum:

            return True

        # Check if left subtree has path sum
        if self.hasPathSum(root.left, targetSum - root.val):

            return True

        # Check if right subtree has path sum
        if self.hasPathSum(root.right, targetSum - root.val):

            return True

        return False
        