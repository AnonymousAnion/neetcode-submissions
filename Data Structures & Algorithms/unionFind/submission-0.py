class UnionFind:
    
    def __init__(self, n: int):
        
        self.par = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, x: int) -> int:
        
        p = self.par[x]

        while p != self.par[p]: # Root ancestor is its own parent

            # Path Compression to optimize subsequent queries
            self.par[p] = self.par[self.par[p]]

            # Ascend ancestor tree
            p = self.par[p]

        print(self.par[x])

        # Return root ancestor of x
        return p

    def isSameComponent(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:

            return False

        # Enforce a balanced Tree on union operations
        if self.rank[p1] > self.rank[p2]:

            self.par[p2] = p1

        elif self.rank[p2] > self.rank[p1]:

            self.par[p1] = p2

        else:

            self.par[p1] = p2
            self.rank[p2] += 1

        return True

    def getNumComponents(self) -> int:

        components = set()

        for n in self.par:

            components.add(self.find(n))

        return len(components)