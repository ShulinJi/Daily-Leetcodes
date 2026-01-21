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

# O(n*m) bc 2 binary search O(m) + O(n) = O(mn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        correct_row = -1
        while left <= right:
            mid = (left + right) // 2
            # if target is bigger than the last element of that row, try other bigger row
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                # we find the condition where matrix[mid][0] < tagret < matrix[mid][-1] 
                correct_row = mid
                break
        # if we get here, it means we found the correct row, then do binary search again to find the exact number
        if correct_row < 0:
            return False

        left = 0
        right = len(matrix[correct_row])
        while left < right:
            mid = (left + right) // 2
            if matrix[correct_row][mid] > target:
                right = mid
            elif matrix[correct_row][mid] == target:
                return True
            else:
                left = mid + 1
        
        return False
                
               


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
