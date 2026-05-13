class UnionFind:
    
    def __init__(self, n: int):
        
        self.par = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
        self.num_components = n

    def find(self, x: int) -> int:
        
        if x != self.par[x]: # Root ancestor is its own parent

            # Path Compression to optimize subsequent queries
            self.par[x] = self.find(self.par[x])

        # Return root ancestor of x
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:

            return False

        # Enforce a balanced Tree on union operations
        if self.size[root_x] > self.size[root_y]:

            self.par[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        else:

            self.par[root_x] = root_y
            self.size[root_y] += self.size[root_x]

        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:

        return self.num_components