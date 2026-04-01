# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def Equal(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p and not q or not p and q:

                return False

            if p and q and p.val != q.val:

                return False

            if p and q:

                if p.left and not q.left or p.right and not q.right or not p.left and q.left or not p.right and q.right:

                    return False

                if p.left and q.left:

                    if not Equal(p.left, q.left):

                        return False

                if p.right and q.right:

                    if not Equal(p.right, q.right):

                        return False

            return True

        return Equal(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if self.isSameTree(root, subRoot): return True

        if root.left and self.isSubtree(root.left, subRoot): return True

        if root.right and self.isSubtree(root.right, subRoot): return True

        return False