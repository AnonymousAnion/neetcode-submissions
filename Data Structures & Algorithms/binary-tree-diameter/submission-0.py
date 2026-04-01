# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # return max depth at node for others' calculations
        # but update the global max depth value based on the 
        # sum of max depths of a node's children.
        max_diameter = 0

        def diameter(node: Optional[TreeNode]) -> int:

            nonlocal max_diameter
            
            if node:

                left_max = 0
                left_max = diameter(node.left)

                right_max = 0
                right_max = diameter(node.right)

                max_diameter = max(max_diameter, left_max + right_max)

                return 1 + max(left_max, right_max)

            return 0

        diameter(root)

        return max_diameter