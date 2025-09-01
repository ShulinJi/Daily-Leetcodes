# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

# O(n^2) time complexity, where n is the number of bars in the histogram. This is because we have a nested loop: for each bar, we potentially look at all other bars to its right to determine the minimum height and calculate the area.
# brute force approach by examining all possible rectangles
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area