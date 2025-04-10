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
        # memorize for the calculated result, key = (index, accumulated_sum)
        mem = {}
        def find_subset(n, current_sum):
            # if current_accumulated sum is target_sum, then we find the answer, return True
            if current_sum == target_sum:
                return True
            
            # if we reach the end of the array and still couln't find answer, then false
            # if current_sum is bigger than target_sum, then we didn't find the answer and since the array doesn't have negative number
            if n == -1 or current_sum > target_sum:
                return False
            
            # if key is in the mem, directly return
            key = (n, current_sum)
            if key in mem:
                return mem[key]

            # then we try either: add the current number to the sum, or continue search without adding current number find_subset(n - 1, current_sum)
            result = find_subset(n - 1, current_sum + nums[n]) or find_subset(n - 1, current_sum)
            mem[key] = result
            
            return result

        # if the total sum cannot be divided by 2, then we cannot find a subset that sums up to total_sum // 2
        total_sum = sum(nums)
        if total_sum % 2:
            return False

        # we try to find a subset that can sum up to total_sum // 2, then the rest is also total_sum // 2, then we subsets are equal
        target_sum = total_sum // 2

        # find the anwser from bottom
        # could also do from the beginning until the end ,doesn't matter
        return find_subset(len(nums) - 1, 0)

        



        