# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mem = {}
        def find_subset(n, current_sum):
            if current_sum == target_sum:
                return True
            
            if n == -1 or current_sum > target_sum:
                return False
            
            key = (n, current_sum)
            if key in mem:
                return mem[key]
            result = find_subset(n - 1, current_sum + nums[n]) or find_subset(n - 1, current_sum)
            mem[key] = result
            
            return result

        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target_sum = total_sum // 2

        return find_subset(len(nums) - 1, 0)

        



        