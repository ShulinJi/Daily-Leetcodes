# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

# O(numRows^2) time, O(numRows) space
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            # create a new row, with the first and last elements as 1, rest as None
            row = [None for _ in range(row_num + 1)]
            row[0] = 1
            row[-1] = 1

            # fill in the middle elements (start after row_num = 2, before it is just [1] and [1, 1])
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            
            triangle.append(row)
        
        return triangle