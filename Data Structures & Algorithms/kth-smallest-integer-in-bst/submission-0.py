# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        k_smallest = root
        early_termination = False
        
        def traverse(node: Optional[TreeNode], count_smaller: int) -> int:

            nonlocal k_smallest
            nonlocal early_termination

            if not node or early_termination:

                return 0

            num_smaller = traverse(node.left, count_smaller)

            #print("Current Node: ", node.val)
            #print("Num Smaller: ", num_smaller + count_smaller)

            if num_smaller + count_smaller == k - 1:

                k_smallest = node
                early_termination = True

            num_smaller += traverse(node.right, count_smaller + num_smaller + 1)

            #print("Returning # Smaller: ", 1 + num_smaller)

            return 1 + num_smaller

        traverse(root, 0)

        return k_smallest.val