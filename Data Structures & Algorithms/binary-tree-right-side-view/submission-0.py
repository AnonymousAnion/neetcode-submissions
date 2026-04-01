# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:

            return []

        # BFS but only return the last element in each level
        queue = deque()
        queue.append(root)
        viewable_from_right = []
        level = 0
        
        while queue:

            viewable_from_right.append(queue[-1].val)

            for i in range(len(queue)):

                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            level += 1

        return viewable_from_right