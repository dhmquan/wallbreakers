#from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.dfs(board, x, y, word):
                    return True
        return False
                    
        
    def dfs(self, board, x, y, word):
        if len(word) == 0:
            return True

        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[0]:
            return False
        
        #temporary flip board[x][y] to keep track of node seen so far
        val = board[x][y]
        board[x][y] = "."
        
        out = (self.dfs(board, x - 1, y, word[1:]) or self.dfs(board, x + 1, y, word[1:])
               or self.dfs(board, x, y - 1, word[1:]) or self.dfs(board, x, y + 1, word[1:]))
        #up = self.dfs(board, x - 1, y, word, i)
        #down = self.dfs(board, x + 1, y, word, i)
        #left = self.dfs(board, x, y - 1, word, i)
        #right = self.dfs(board, x, y + 1, word, i)
        
        board[x][y] = val
        
        #return up or down or left or right
        return out