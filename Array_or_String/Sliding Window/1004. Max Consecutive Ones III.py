# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


# My own solution by shrinking the window size, runtime still O(n)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        ans = 0
        while right < len(nums):
            # if we see a 0, then exhaust an available 0
            if nums[right] == 0:
                k -= 1

            # if there isn't any 0 can be used, we need to move left inorder to find new longest 1's so that the subarray is legal(k >= 0, we did not use more than k 0's)
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans