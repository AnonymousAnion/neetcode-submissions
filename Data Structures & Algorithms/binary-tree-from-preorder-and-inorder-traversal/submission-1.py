# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mapping = {val: index for index, val in enumerate(inorder)}

        pre_idx = 0

        def dfs(l, r):

            # Key Observation: The tree has the actual values in the
            # same relative order as the pre-order traversal. You just need
            # to know when to fill in between them with null values.

            # Overall Idea: Pre-Order Traversal with l and r bounds.
            # The split is determined by the mapping of the preorder value
            # within the inorder traversal

            # 3 Key Implementation ideas:
            # 1.) Pre-Order traversal
            # 2.) Subtree indices known from inorder mapping of preorder index
            # 3.) Return None when the pre-order traversal would be violated
            # by the subtrees indicated by the inorder traversal which indicate
            # ranges for indices found in the left and right subtree. This creates
            # any necessary null filling in the tree. Only add the next node in the
            # pre-order traversal when it is a valid value as indicated by the limitations
            # imposed the left / right subtrees of the parent. Increment the pre-order
            # index to be ready to access the next pre-order index when its time comes.

            nonlocal pre_idx

            if l > r:

                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = mapping[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
