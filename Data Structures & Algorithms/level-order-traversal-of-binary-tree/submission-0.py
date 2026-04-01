# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:

            return []

        level_order_traversal = []
        queue = deque()
        queue.append(root)
        level = 0

        while queue:

            level_order_traversal.append([])

            for i in range(len(queue)):

                node = queue.popleft()
                level_order_traversal[level].append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            level += 1

        return level_order_traversal