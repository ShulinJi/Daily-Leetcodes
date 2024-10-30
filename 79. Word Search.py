class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        # check each entry starting with first letter of word
        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == word[0]:
                    if self.backtrack(row, col, word):
                        return True
                else:
                    continue
        return False

    def backtrack(self, row, col, suffix):
        # if we have reached all the letters, we return True since we find all letters
        if len(suffix) == 0:
            return True
        # check if row and col are out of bound and check if the letter is expected one, if not return False
        if (col < 0 or row < 0 or row == self.m or col == self.n or self.board[row][col] != suffix[0]):
            return False

        # set the status to false for beginning
        ret = False
        # replace the letter to '#' so that it won't backtrack to our current place ('ABCDEF', for saying we are at B from A, we don't want to go back to A because that's invalid)
        # We just mark our track to # to avoid duplicate use
        self.board[row][col] = '#'

        # We check for 4 directions and see if it is a dead end
        for row_dr, col_dr in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
            ret = self.backtrack(row + row_dr, col + col_dr, suffix[1:])
            if ret == True:
                break
        # change our status back after we hit the end
        self.board[row][col] = suffix[0]

        return ret
        
            
