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

# SECOND ATTEMPT, similar to DP approach
class Solution:
    def trap(self, height):
        # O(n) and O(1)
        left = 0
        right = len(height) - 1

        rightmost = 0
        leftmost = 0
        ans = 0
        # similar to DP approach, but we only need to know that if there is a larger bar  at one end, we are gurannteed
        # to have some water trapped and it depends on the shorter bar (current direction(pointer)), tha's why we have two pointer, we can account both from left and right, if left is larger, then we calculate for right, if right is larger, we start to calulate left!
        while left < right:
            if height[left] < height[right]:
                leftmost = max(leftmost, height[left])
                ans += leftmost - height[left]
                left += 1
            else:
                rightmost = max(rightmost, height[right])
                ans += rightmost - height[right]
                right -= 1
        
        return ans


# O(n) and O(n) using DP (pre-populate results)
class Solution:
    def trap(self, height):
        # O(n) and O(n)
        if len(height) == 0:
            return 0
        
        ans = 0
        n = len(height)
        leftmost = [0] * n
        rightmost = [0] * n

        # needs init because we need to check i - 1 element
        # populate the left boundary for the current index
        leftmost[0] = height[0]
        for i in range(1, n):
            leftmost[i] = max(height[i], leftmost[i - 1])

        # populate the right boundary for current index, from backward because of the right boundary
        rightmost[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightmost[i] = max(height[i], rightmost[i + 1])
        
        # answer is the min of the left and right boundary which can hold the water and then subtract the height
        for i in range(1, n - 1):
            ans += min(rightmost[i], leftmost[i]) - height[i]
        
        return ans

# O(n^2) and O(n), for each index, finding the min b/w right and left boundary and subtract the height is the trpped water for that index
class Solution:
    def trap(self, height):
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0
            # Search the left part for max bar size

            # find left max for current point
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            # Search the right part for max bar size
            for j in range(i, size):
                right_max = max(right_max, height[j])
            
            # the current water trapped in current index
            ans += min(left_max, right_max) - height[i]
        return ans
