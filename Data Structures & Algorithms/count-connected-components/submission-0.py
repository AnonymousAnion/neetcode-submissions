class UnionFind:

    def __init__(self, n: int):

        self.parent = [i for i in range(n)]
        self.num_elements = [1] * n
        self.ccs = n

    def find(self, x: int) -> int:

        # Path Compression
        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:

        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:

            return False

        # Union Tree Balancing
        if self.num_elements[root_x] > self.num_elements[root_y]:

            self.parent[root_y] = root_x
            self.num_elements[root_x] += self.num_elements[root_y]

        else:

            self.parent[root_x] = root_y
            self.num_elements[root_y] += self.num_elements[root_x]

        self.ccs -= 1
        return True

    def get_num_ccs(self) -> int:

        return self.ccs

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        ds = UnionFind(n)

        for edge in edges:

            src, dst = edge
            ds.union(src, dst)

        return ds.get_num_ccs()
        