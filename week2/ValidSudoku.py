class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check all rows
        for row in board:
            numbers = set()
            for x in row:
                if not self.isValidSub(x, numbers):
                    return False

        #check all columns
        for j in range(len(board[0])):
            numbers = set()
            for i in range(len(board)):
                x = board[i][j]
                if not self.isValidSub(x, numbers):
                    return False

        #check all sub-boxes
        for box_i in range(0, len(board), 3):
            for box_j in range(0, len(board[0]), 3):
                numbers = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        #print("checking " + str(i + box_i) + " and " + str(j + box_j))
                        x = board[i + box_i][j + box_j]
                        if not self.isValidSub(x, numbers):
                            return False
        
        return True
        
    def isValidSub(self, x: str, numbers: set) -> bool:
        if (x != ".") and (x in numbers):
            return False
        numbers.add(x)
        return True