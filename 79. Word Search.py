class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        for row in range(self.m):
            for col in range(self.n):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True
        if (col < 0 or row < 0 or row == self.m or col == self.n or self.board[row][col] != suffix[0]):
            return False
        
        ret = False
        self.board[row][col] = '#'

        for row_dr, col_dr in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
            ret = self.backtrack(row + row_dr, col + col_dr, suffix[1:])
            if ret == True:
                break
            
        self.board[row][col] = suffix[0]

        return ret
        
            
