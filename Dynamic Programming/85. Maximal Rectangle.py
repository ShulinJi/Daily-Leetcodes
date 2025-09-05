# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

# O(m * n) time complexity
# O(n) space complexity
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # leetcode 84: Largest Rectangle in Histogram
        def find_max_area_histogram(heights):
            stack = [-1]
            max_area = 0
            for i in range(len(heights)):
                # found a right limit at i, pop
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    curr_height = heights[stack.pop()]
                    # right limit is i, left limit is stack[-1] because it is the first one smaller than curr_height
                    curr_width = i - stack[-1] - 1
                    max_area = max(max_area, curr_height * curr_width)
                stack.append(i)

            # we have some left that right limit is not found (it is smallest from his on to the end)
            while stack[-1] != -1:
                curr_height = heights[stack.pop()]
                curr_width = len(heights) - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            
            return max_area

        if not matrix:
            return 0

        # dp[j] := the height of histogram at column j or the max consecutive 1s at column j ending at row i, it is column wise
        dp = [0] * len(matrix[0])
        maxarea = 0
        # O(N)
        for i in range(len(matrix)):
            # O(M)
            for j in range(len(matrix[0])):
                # update the height of histogram at column j for each row i
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            # each time we update the histogram, we find the max area in it again
            # O(M) time complexity
            maxarea = max(maxarea, find_max_area_histogram(dp))
        
        return maxarea

# O(m * n * n) time complexity (m*n for traversing the matrix, n for traversing upwards to find the max area)
# O(m * n) space complexity
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        # dp[i][j] := the maximum width (max consecutive 1s at row i) of 1's ending at (i, j)
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # skip 0's
                if matrix[i][j] == "0":
                    continue

                # compute the maximum width and update dp with it
                # compute the maximum consecutive 1s at row i ending at (i, j)
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                # traverse upwards to find the maximum area
                # width is the minimum width of 1s from row i to row k
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea