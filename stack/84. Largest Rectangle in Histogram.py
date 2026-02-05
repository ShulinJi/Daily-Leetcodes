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

# SECOND ATTEMPT
# O(n) time and O(n) space
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the stack is increasing order, so that whenever we find a number
        stack = [-1]
        ans = 0

        for i in range(len(heights)):
            # we found a new right boundary, (we don't account for left and right boundary, the middle part are the area we try to calculate)
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                ans = max(ans, current_height * current_width)
            # add current bar to the stack
            stack.append(i)

        
        # it means we have some bars that never see a smaller bar(right boundary) that are left over, right boundary for them is len(heights)
        while stack [-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            ans = max(ans, current_width * current_height)
        
        return ans

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

# O(n) time complexity, where n is the number of bars in the histogram. Each bar is pushed and popped from the stack at most once.
# using a stack to keep track of indices of the bars in ascending order
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use -1 because the left limit could be -1 (no left limit) for cases like it is min height for all bars to the left
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            # found a smaller value (right limit for current height)
            # we keep storing indices of heights in ascending order in the stack and until we find a smaller height, then we start to pop from the stack
            # which means we found the right limit for the popped height, and left limit is the new top of the stack after popping
            # since new top of the stack after popping is the first height smaller than the popped height
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                # pop the height as the current height
                current_height = heights[stack.pop()]
                # right limit - left limit - 1 is the width, use -1 becuase we want to exclude the left limit and right limit, ex left=2, right=4, then 
                # width = 4 - 2 - 1 = 1, which is the index of the bar between left and right
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_width * current_height)
            stack.append(i)

        # after iterating through all heights, we may still have some heights in the stack
        # which means they don't have a right limit, so we can use the length of heights as the right limit
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            # use right most boundary as right limit since all elements left in the stack are the ones couldn't find 
            # smaller heights than them, which means it is min height after its index
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        
        return max_area
