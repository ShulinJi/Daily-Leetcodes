# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

# O(n) time and O(1) space
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        dup = 0
        missing = 0
        # For each number we encounter, we flip the sign of the number at the index corresponding to that number
        # If we encounter a number whose corresponding index is already negative, it means we've seen that number before (duplicate)
        # the array should end up with one positive number and the rest negative numbers
        # After processing all numbers, the index which has a positive value indicates the missing number
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
                # can't break ear;y because we haven't traversed the whole array and the positive numbers left in 
                # the array could mess up the missing numbers
            else:
                nums[abs(n) - 1] *= -1
        
        # find the index which has a positive value, that index + 1 is the missing number because the numbers are from 1 to n not 0 to n-1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
        
        return [dup, missing]
