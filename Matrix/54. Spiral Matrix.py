# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bot = len(matrix) - 1

        returnList = []
        while left <= right and top <= bot:
            # first the top row
            for i in range(left, right + 1):
                returnList.append(matrix[top][i])
            top += 1

            # then the right-most column
            for i in range(top, bot + 1):
                returnList.append(matrix[i][right])
            right -= 1

            # then bottom row
            if left <= right and top <= bot:
                for i in range(right, left - 1, -1):
                    returnList.append(matrix[bot][i])
                bot -= 1
            
            # then left-most column
            if left <= right and top <= bot:
                for i in range(bot, top - 1, -1):
                    returnList.append(matrix[i][left])
                left += 1
            
        
        return returnList






        top = 0
        bot = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        returnList = list()
        while top <= bot and left <= right:
            for i in range(left, right + 1):
                returnList.append(matrix[top][i])
            top += 1
            
            for i in range(top, bot + 1):
                returnList.append(matrix[i][right])
            right -= 1
            
            if top <= bot:
                for i in range(right, left - 1, -1):
                    returnList.append(matrix[bot][i])
                bot -= 1
            
            if left <= right:
                for i in range(bot, top - 1, -1):
                    returnList.append(matrix[i][left])
                left += 1
                    
        return returnList