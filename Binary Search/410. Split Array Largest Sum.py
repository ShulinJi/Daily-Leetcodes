# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= k <= min(50, nums.length)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # as we iterate over each element, we must decide whether to add the element to the current subarray or to start a new subarray. This decision will depend on the number of subarrays we have already made. In other words, each decision we make is affected by the previous decisions we have made. Second, the problem is asking to minimize the largest sum of subarrays.
        def min_subarray_required(max_sum):
            current_sum = 0
            splits_required = 0

            for element in nums:
                if current_sum + element <= max_sum:
                    current_sum += element
                else:
                    current_sum = element
                    splits_required += 1
            
            return splits_required + 1
        
        left = max(nums)
        right = sum(nums)
        minimum_largest_split_sum = None

        while left <= right:
            max_allowed = (left + right) // 2
            if min_subarray_required(max_allowed) <= k:
                right = max_allowed - 1
                minimum_largest_split_sum = max_allowed
            else:
                left = max_allowed + 1
        
        return minimum_largest_split_sum
        