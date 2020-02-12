class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        
        h = len(board)
        w = len(board[0])
        
        uf = UnionFind(h * w + 1)
        outside = h * w
        
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    continue
                
                x = j + i * w
                
                if (i == 0) or (i == h - 1) or (j == 0) or (j == w - 1):
                    uf.Union(x, outside)
                    continue
                    
                self.adjacentUnion(board, i, j, uf, x)
             
        root_outside = uf.Find(outside)
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    continue
                
                x = j + i * w
                if uf.Find(x) != root_outside:
                    board[i][j] = 'X'
                
                    
    def adjacentUnion(self, board: List[List[str]], i: int, j: int, uf, x:int):
        w = len(board[0])
        if (j > 0) and (board[i][j-1] == 'O'):
            y = (j-1) + i * w
            uf.Union(x, y)
        if (i > 0) and (board[i-1][j] == 'O'):
            y = j + (i-1) * w
            uf.Union(x, y)
        if (j < len(board[0]) - 1) and (board[i][j+1] == 'O'):
            y = (j+1) + i * w
            uf.Union(x, y)
        if (i < len(board) - 1) and (board[i+1][j] == 'O'):
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