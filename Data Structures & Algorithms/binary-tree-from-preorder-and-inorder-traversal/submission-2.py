# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mappings = {val: index for index, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(l, r):

            nonlocal pre_idx

            if l > r: # Pre-order traversal not valid based on in-order subtrees

                return None

            # Pre-order traversal valid based on in-order subtrees
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            m = mappings[root_val]
            root.left = dfs(l, m -1)
            root.right = dfs(m + 1, r)

            return root

        return dfs(0, len(preorder) - 1)