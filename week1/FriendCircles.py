class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0
        
        uf = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    uf.Union(i, j)
        
        circleNum = 0
        for i in range(len(M)):
            if uf.parent[i] == i:
                circleNum += 1
                
        return circleNum
        
        
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
        else:
            self.parent[root_x] = root_y