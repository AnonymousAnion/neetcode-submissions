# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def find_ancestors(val: int, ancestors: List[int]) -> None:

            current = root

            while current:

                if val < current.val:

                    current = current.left 

                elif val == current.val:

                    return

                else:

                    current = current.right 

                if current: ancestors.append(current)

        # Find P and record its ancestors in height order from root
        # O(h) time complexity
        # O(h) space
        p_ancestors = [root]
        find_ancestors(p.val, p_ancestors)
        #print("P Ancestors: ", p_ancestors)

        # Find Q and record its ancestors in height order from root
        # O(h) time complexity
        # O(h) space
        q_ancestors = [root]
        find_ancestors(q.val, q_ancestors)
        #print("Q Ancestors: ", q_ancestors)

        # Iteratively compare ancestors in order to find the lowest descendant
        # O(h) time complexity
        lowest_common_ancestor = root

        for i in range(min(len(p_ancestors), len(q_ancestors))):

            if p_ancestors[i].val == q_ancestors[i].val:

                lowest_common_ancestor = p_ancestors[i]

            else:

                return lowest_common_ancestor

        return lowest_common_ancestor