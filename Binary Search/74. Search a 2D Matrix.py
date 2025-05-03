# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# my own solution in Log(m * n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search to find the correct row
        # Use O(log m)
        left = 0
        right = len(matrix)

        while left < right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                # if we get to this section, it means we have found the correct row that row[0] target < row[-1]
                # then we do a second binary search that find matrix[mid][i] that if there's any number == target 
                left = 0
                right = len(matrix[0])
                while left < right:
                    inner_mid = (left + right) // 2
                    if target == matrix[mid][inner_mid]:
                        return True
                    elif target < matrix[mid][inner_mid]:
                        right = inner_mid
                    else:
                        left = inner_mid + 1

        return False