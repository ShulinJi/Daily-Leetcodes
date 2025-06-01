# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# pre-compute the leftmost and rightmost using DP, O(n) runtime, O(n) space
class Solution:
    def trap(self, height):
        leftmost = [0] * len(height)
        rightmost = [0] * len(height)
        ans = 0

        leftmost[0] = height[0]
        rightmost[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            rightmost[i] = max(rightmost[i + 1], height[i])
        for i in range(1, len(height)):
            leftmost[i] = max(height[i], leftmost[i - 1])

        for i in range(len(height)):
            ans += min(rightmost[i], leftmost[i]) - height[i]
        
        return ans


# brute force, O(n^2) runtime
class Solution:
    def trap(self, height):
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0
            # Search the left part for max bar size
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            # Search the right part for max bar size
            for j in range(i, size):
                right_max = max(right_max, height[j])
            ans += min(left_max, right_max) - height[i]
        return ans