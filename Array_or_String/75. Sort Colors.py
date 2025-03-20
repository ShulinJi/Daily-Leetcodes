# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, p2 = 0, len(nums) - 1

        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                # we find 0, then swap curr and p0 since p0 starts at leftest and whenever we add a 0
                # we just increment p0 to indicate that we have found a 0
                nums[p0], nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            elif nums[curr] == 1:
                # and if 0 and 2 are taken care, then 1 will just be at the centre
                curr += 1
            else:
                #  we met 2, then swap it with p2, and decrement p2 by 1
                # p2 starts at rightest and decrement 1 means, we find a 2 and the more 2 we find,
                # the more decrement we use for p2
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        