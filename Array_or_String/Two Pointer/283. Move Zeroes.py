# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            # whenever we find a non zero number, we switch it with the slow
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
        

# O(n) and O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_found_at = 0

        # first pass: move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                # last_non_zero_found_at used to track the non-zero numbers index and then after the 
                # iteration, last_non_zero_found_at will be at the place where zero begins
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        # fill the rest with zeros
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0

    
