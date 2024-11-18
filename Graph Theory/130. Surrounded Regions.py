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


