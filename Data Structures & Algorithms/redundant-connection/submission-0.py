class UnionFind:

    def __init__(self, n: int):

        self.parent = {i: i for i in range(1, n + 1)}
        self.components = {i: 1 for i in range(1, n + 1)}
        self.num_components = n

    def find(self, x: int) -> None:

        # Find the parent of the indicated node, x.

        if self.parent[x] != x: # Root node is its own parent

            # Path Compression
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:

        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:

            return False

        # Minimize Tree Height on Union Joins
        if self.components[root_x] > self.components[root_y]:

            self.parent[root_y] = root_x
            self.components[root_x] += self.components[root_y]

        else:

            self.parent[root_x] = root_y
            self.components[root_y] += self.components[root_x]

        self.num_components -= 1
        return True

    def num_components(self) -> int:

        return self.num_components

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = UnionFind(len(edges))
        removed_edge = []

        for edge in edges:

            src, dst = edge

            if not graph.union(src, dst):

                removed_edge = [src, dst]

        return removed_edge
        