# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# O(n^2) time complexity solution using prefix sums. O(n) space complexity.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        # build prefix‐sum array of length n+1
        # sums[i] = sum of nums[0..i-1], so sums[0]=0
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        # for each (start, end] interval, check if sum == k
        for start in range(n):
            for end in range(start + 1, n + 1):
                if sums[end] - sums[start] == k:
                    count += 1

        return count
