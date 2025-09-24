# This question is about implementing a basic elimination algorithm for Candy Crush.

# Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

# The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

# If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the stable board.

 

# Example 1:


# Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
# Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
# Example 2:

# Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
# Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 3 <= m, n <= 50
# 1 <= board[i][j] <= 2000


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])

        # find all positions to be crushed
        def find():
            crush_set = set()
            # check horizontally 
            for r in range(1, m - 1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue
                    # check if the current position and the one above and below are the same, if so, add them to the crush set
                    if board[r][c] == board[r - 1][c] == board[r + 1][c]:
                        crush_set.add((r, c))
                        crush_set.add((r + 1, c))
                        crush_set.add((r - 1, c))
            
            # check vertically
            for r in range(m):
                for c in range(1, n - 1):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r][c + 1] == board[r][c - 1]:
                        crush_set.add((r, c))
                        crush_set.add((r, c + 1))
                        crush_set.add((r, c - 1))
            
            return crush_set

        # drop the candies that are above the crushed positions, 
        def drop():
            # traverse vertically column by column
            for c in range(n):
                # lowest index of zero in the current column
                lowest_zero = -1
                for r in range(m - 1, -1, -1):
                    # if we find a zero, update the lowest index of zero (the one closest to the bottom)
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)
                    # if we find a non-zero and there is a zero below it, swap them
                    # Use >= 0 is enough because we are traversing from bottom to top, so lowest_zero will always be smaller than r, 
                    # which means the non-zero we found is always above the lowest zero, then we need to swap them
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        # after swapping, the lowest zero is now one row above
                        lowest_zero -= 1

        # crush the candies in the crush set by setting them to 0
        def crush(curshed_set):
            for (r, c) in crushed_set:
                board[r][c] = 0
        
        # repeat the process until no more candies can be crushed
        crushed_set = find()
        while crushed_set:
            # three phases: find, crush, drop
            crush(crushed_set)
            drop()
            crushed_set = find()
        
        return board