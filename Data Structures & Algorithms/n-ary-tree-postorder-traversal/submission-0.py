"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        traversal = []

        def dfs(node) -> None:

            if not node:

                return

            nonlocal traversal

            for child in node.children:

                dfs(child)

            traversal.append(node.val)

        dfs(root)

        return traversal