class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        
        uf = UnionFind(h * w)
        for i in range(h):
            for j in range(w):
                x = j + i * w
                
                if grid[i][j] == '0':
                    uf.parent[x] = -1
                    continue
                
                self.adjacentUnion(grid, i, j, uf, x)
                    
                    
        out = 0
        for i in range(len(uf.parent)):
            if (uf.parent[i] == i):
                out += 1
        return out

    def adjacentUnion(self, grid: List[List[str]], i: int, j: int, uf, x:int):
        w = len(grid[0])
        if (j > 0) and (grid[i][j-1] == '1'):
            y = (j-1) + i * w
            uf.Union(x, y)
        if (i > 0) and (grid[i-1][j] == '1'):
            y = j + (i-1) * w
            uf.Union(x, y)
        if (j < len(grid[0]) - 1) and (grid[i][j+1] == '1'):
            y = (j+1) + i * w
            uf.Union(x, y)
        if (i < len(grid) - 1) and (grid[i+1][j] == '1'):
            y = j + (i+1) * w
            uf.Union(x, y)
                
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def Find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]
    
    def Union(self, x, y):
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1