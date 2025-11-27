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

# O(n) time complexity solution using a hashmap to store the frequency of prefix sums. O(n) space complexity.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum: sums[i] = sum of nums[0..i], freq: frequency of prefix sums
        # the case that sums == k is already covered when sums - k == 0, that's why we initialize freq[0] = 1
        freq = {0:1}
        count = 0
        sums = 0
        # keep track of prefix sum, and whenever we find a sum - k, we add how many times that sum - k have occurred in the hashmap
        # because the counter represents how many different ways of subarray we can form that sum - k.
        for i in range(len(nums)):
            sums += nums[i]
            # if there is a prefix sum that equals to sums - k, then there is a subarray that sums to k
            #  The reason that we keep accumulating the count is that there could be multiple prefix sums that equal to sums - k
            # h[sums - k] gives us the number of times that prefix sum has occurred so far (how many different subarrays ending at the current index sum to k)
            # h[curr_sum - k] = how many different “paths” (prefix sums) we’ve seen before that, when paired with the current end, give us a subarray of sum k
            # “Every prefix occurrence is a possible checkpoint. As the end moves, each checkpoint spawns a new subarray — so we keep accumulating, not resetting.”
            #  it's like slicing the array at different points to form subarrays that sum to k, and we are recording the checkpoint


            # it means we try to find value corresponding to key (sums - k), if we can't find it, return defualt 0
            count += freq.get(sums - k, 0)
            freq[sums] = freq.get(sums, 0) + 1 
        return count

# Brute force solution by checking all subarrays.
# O(n^2) time complexity, where n is the length of the nums array.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sums = 0
            for j in range(i, len(nums)):
                sums += nums[j]
                if sums == k:
                    count += 1
        
        return count

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
