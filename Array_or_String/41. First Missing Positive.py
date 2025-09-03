# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contains1 = False
        for i in range(len(nums)):
            if nums[i] == 1 and contains1 == False:
                contains1 = True
            elif nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        
        if contains1 == False:
            return 1
        
        for i in range(len(nums)):
            value = abs(nums[i])
            if value == len(nums):
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])
        
        # try to find the first missing positive
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        
        # nums[0] store the information of whether n exists
        # since after traverse, nums[0] won't be touched unless we see number n (len(nums)), and make it negative
        if nums[0] > 0: 
            return len(nums)
        
        # if all of above satifies, it means that we have covered the range from 1 -- n (len(nums))
        # then the only possible number is n + 1
        return len(nums) + 1


# O(n) time complexity, where n is the length of the input array nums. We traverse the array a constant number of times.
# O(n) space complexity, where n is the maximum value in the input array nums
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # + 2 to account for the case when all numbers from 1 to max(nums) are present and we need to return max(nums) + 1 
        # if the first missing positive is max(nums) + 1 eg. [1,2,3] -> 4
        check_array = [False] * (max(nums) + 2)

        for num in nums:
            if num > 0:
                check_array[num] = True
        
        for i in range(1, len(check_array)):
            if check_array[i] == False:
                return i
        