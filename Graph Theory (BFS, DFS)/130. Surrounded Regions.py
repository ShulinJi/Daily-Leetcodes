# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


# SECOND ATTEMPT
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # O(n) because number of cells N in the board (worst case traverse all cells twice, dfs worst case only traverse board once), and O(n) because number of cells (list of boarders if all cells are boarders, max depth of recursive call is N calls)
        """
        Do not return anything, modify board in-place instead.
        """
        # it is obvious that if any "O" can reach the border, then it is an escape and will not be captured.
        # Then we can check the border instead of check the whole border, which saves a huge amount of time. then we first get all the cells on the border(edges)

        border = []
        self.ROW = len(board)
        self.COL = len(board[0])

        for r in range(self.ROW):
            for c in range(self.COL):
                if r == 0 or r == self.ROW - 1 or c == 0 or c == self.COL - 1:
                    border.append((r, c))
        
        # dfs only traverse along the O and mark all the O that can be reached from the edge to E
        def dfs(row, col):
            # if we meet X or E, we return , we meet E we meet duplicate, we meet X, we meet barrier
            if board[row][col] != "O":
                return 
            
            board[row][col] = "E"
            if col < self.COL - 1:
                dfs(row, col + 1)
            if col > 0:
                dfs(row, col - 1)
            if row < self.ROW - 1:
                dfs(row + 1, col)
            if row > 0:
                dfs(row - 1, col)              

        # now we run the dfs from the border
        for r, c in border:
            dfs(r, c)

        # now we change all the E to O since they are noe captured, not surrounded bc they can be reached from edge, and any other O would be captured!
        for r in range(self.ROW):
            for c in range(self.COL):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        


        


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Works DFS, but too slow
        # def dfs(row, col):
        #     if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 'X' or board[row][col] == '#':
        #         return "Capture"
            
        #     if row == len(board) - 1 or row == 0 or col == 0 or col == len(board[0]) - 1:
        #         return "No Capture"
        #     elif board[row + 1][col] == 'O' and board[row - 1][col] == 'O' and board[row][col + 1] == 'O' and board[row][col - 1] == 'O':
        #         return "No Capture"
        #     else:
        #         board[row][col] = '#'
            
        #     next_move1 = dfs(row + 1, col)
        #     next_move2 = dfs(row - 1, col)
        #     next_move3 = dfs(row, col + 1)
        #     next_move4 = dfs(row, col - 1)

        #     if next_move1 == "No Capture" or next_move2 == "No Capture" or next_move3 == "No Capture" or next_move4 == "No Capture":
        #         board[row][col] = 'O'
        #         return "No Capture"
        #     else:
        #         return "Capture"

            
        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         if board[row][col] == 'O':
        #             status = dfs(row, col)
        #             for x in range(len(board)):
        #                 for y in range(len(board[0])):
        #                     if board[x][y] == '#':
        #                         if status == "No Capture":
        #                             board[x][y] = 'O'
        #                         else:
        #                             board[x][y] = 'X'


        # DFS, but we start from the 'O' that are at the edge and we mark the 'O' s hat are reachable with "E" so that we flip it later and the other "O" s are surrounded!
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1). retrieve all border cells
        borders = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                if x == len(board) - 1 or x == 0 or y == 0 or y == len(board[0]) - 1:
                    borders.append([x, y])

        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        # In this approach we run fewer runs by only running from the ones that are already in the edges and mark those the ones we can reach to E that we will flip later, if they remain 'O', then it means it is not reachable from the edge and then it is surrounded. 
        for row, col in borders:
            self.DFS(board, row, col)

        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # captured
                elif board[r][c] == "E":
                    board[r][c] = "O"  # escaped

    def DFS(self, board: List[List[str]], row: int, col: int) -> None:
        # if it is "E" or "X", return 
        if board[row][col] != "O":
            return
        # We mark O to be E, since we are able to reach it
        board[row][col] = "E"
        if col < self.COLS - 1:
            self.DFS(board, row, col + 1)
        if row < self.ROWS - 1:
            self.DFS(board, row + 1, col)
        if col > 0:
            self.DFS(board, row, col - 1)
        if row > 0:
            self.DFS(board, row - 1, col)


