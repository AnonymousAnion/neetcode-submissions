# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node: Optional[TreeNode]) -> None:

            if node:

                # Invert: a.k.a. switch childrens' positions
                temp = node.left
                node.left = node.right
                node.right = temp

                if node.left:

                    traverse(node.left)

                if node.right:

                    traverse(node.right)

        traverse(root)

        return root