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


