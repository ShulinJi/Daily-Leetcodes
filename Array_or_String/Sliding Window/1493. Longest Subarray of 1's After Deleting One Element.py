# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# second attempt, O(n) time, O(1) space, sliding window
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        # zero counts
        zero = 0
        for right in range(len(nums)):
            # if nums[right] == 1, ignore just keep updating the answer and traversing
            if nums[right] == 0:
                zero += 1
            
            # if there are more than 1 zero
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            # use right - left because we have to remove 1 element, it should be (right - left + 1) - 1
            ans = max(ans, right - left)
        
        return ans

# more efficient by memorizing the last_zero_index
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        last_zero_index = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                left = last_zero_index + 1
                last_zero_index = right
            ans = max(ans, right - left)
        return ans

# more generalzied approachj by counting number of zeros 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left)
        
        return max_len
