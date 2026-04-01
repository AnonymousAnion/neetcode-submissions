# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, node: Optional[Treenode]) -> Optional[TreeNode]:

            while node and node.left:

                node = node.left

            return node


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:

            return None

        if key > root.val:

            root.right = self.deleteNode(root.right, key)

        elif key < root.val:

            root.left = self.deleteNode(root.left, key)

        else: # Delete this node

            if not root.left:

                return root.right
            
            elif not root.right:

                return root.left

            else: # Two Children

                # Swap the minimum right descendant with the current node
                min_right = self.findMinNode(root.right)
                root.val = min_right.val
                root.right = self.deleteNode(root.right, min_right.val)

        return root


