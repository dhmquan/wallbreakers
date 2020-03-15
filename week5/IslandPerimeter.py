class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x = 0
        y = 0
        #look for the first island cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = i
                y = j
                if grid[x][y] == 1:
                    break
            if grid[x][y] == 1:
                    break
        
        stack = []
        stack.append((x,y))
        out = 0
        while stack:
            x, y = stack.pop()
            add = self.addEdges(grid, x, y, stack)
            #print("(%d,%d): %d" % (x, y, add))
            out += add
        
        return out
        
        
    def addEdges(self, grid, x, y, stack):
        if grid[x][y] == -1:
            return 0
        out = 0
        out += self.addCell(grid, x - 1, y, stack)
        out += self.addCell(grid, x + 1, y, stack)
        out += self.addCell(grid, x, y - 1, stack)
        out += self.addCell(grid, x, y + 1, stack)
        grid[x][y] = -1
        return out
    
    def addCell(self, grid, x, y, stack):
        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]):
            return 1
        
        val = grid[x][y]
        if val == 0:
            return 1
        elif val == 1:
            stack.append((x, y))
        return 0