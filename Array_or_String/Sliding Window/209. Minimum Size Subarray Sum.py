# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float("inf")
        current_sum = 0
        left = 0

        for i in range(len(nums)):
            # we add right side to the total sum
            current_sum += nums[i]
            # and we try to shrink the array as much as possible from left
            while current_sum >= target:
                # get the current size first before moving left b/c after moving left, it might not be a valid subarray anymore!
                min_length = min(min_length, i - left + 1)
                
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length