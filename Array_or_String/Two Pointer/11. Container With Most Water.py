# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1



class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVolume = 0

        # Proof of the method: https://leetcode.com/problems/container-with-most-water/solutions/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm/
        # we move the short height one, which is more beneficial since the height is limited by short height.
        while left < right:
            # Compute the volume
            currentVolume = (right - left) * min(height[right], height[left])
            if currentVolume > maxVolume:
                maxVolume = currentVolume
            # move the short height one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxVolume