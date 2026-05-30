# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val
        
        def binary_search(node: Optional[TreeNode]) -> None:

            if not node:

                return

            nonlocal closest
            nonlocal target

            if abs(node.val - target) < abs(closest - target):

                closest = node.val

            elif node.val < target and abs(node.val - target) == abs(closest - target):

                closest = node.val

            if target < node.val:

                binary_search(node.left)

            elif target > node.val:

                binary_search(node.right)

        binary_search(root)

        return closest