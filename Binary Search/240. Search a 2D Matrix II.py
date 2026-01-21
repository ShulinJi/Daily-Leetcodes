# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109

# O(m + n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this is different from the 2D matrix question by the matrix that each row is not strictly bigger than prev row
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = m - 1
        col = 0
        # we find that if we start from the bottom left corner, if we go up, we are decreasing, and if we go to the right
        # we are increasing, so we just need to adjust the row and col based on the target
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        
        return False


# O(MxN)
# the enxt row/column is not entirely bigger/smaller than previous one, so 2 binary search does not work here
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        
        # start from top right corner, we can start from either corner, just change the col/row +-
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            # we move to a smaller element col -= 1, because these rules
            # All the integers in each row are sorted in ascending order.
            # All the integers in each column are sorted in ascending order.
            elif matrix[row][col] > target:
                col -= 1
            # we move to the bigger element, to the right of the element
            else:
                row += 1
        
        return False
