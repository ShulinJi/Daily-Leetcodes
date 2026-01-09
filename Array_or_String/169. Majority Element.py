# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        # majority is over half of the elements, then the candidate count would always be equal or greater than 0
        for x in nums:
            # if count is smaller than 0, we switch the candidate
            if count < 0:
                candidate = x
            # if it is first element, simply overwrite
            if candidate == None:
                candidate = x
            # if same element, we increment counter by 1
            elif candidate == x:
                count += 1
            else:
                count -= 1
        
        return candidate


# O(n) and O(n) solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter()
        for num in nums:
            count[num] += 1
        # find the max count in the dictionary
        return max(nums, key=count.get)
