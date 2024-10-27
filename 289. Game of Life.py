# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]
        m = len(board)
        n = len(board[0])
        
        for row in range(m):
            for col in range(n):
                # count how many living cells are nearby
                living_count = 0
                for direction_row, direction_col in directions:
                    updated_row = row + direction_row
                    updated_col = col + direction_col
                    # Use abs here because 2 is converted by 0, we don't count it
                    # And -1 is converted by 1, we still count it, so asb(-1) = 1, still being counted
                    if m > updated_row >= 0 and n > updated_col >= 0 and abs(board[updated_row][updated_col]) == 1:
                        living_count += 1
                print((row, col))
                print(living_count)
                # rule 4 and set it to 2 to avoid interfere with further living counts
                if board[row][col] == 0 and living_count == 3:
                    board[row][col] = 2
                # rule 1 and 3, set it to -1 to avoid futher interference with living counts 0 or 1
                if board[row][col] == 1 and (living_count < 2 or living_count > 3):
                    board[row][col] = -1

        for row in range(m):
            for col in range(n):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


