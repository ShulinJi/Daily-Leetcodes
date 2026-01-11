# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# SECOND ATTEMPT O(n) and O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # avoid the Gauss formula,O(n) and O(1)

        # actual sum of the list 
        curr_sum = 0
        # expected sum if no missing number
        expected_sum = 0

        for i in range(len(nums)):
            # curr_sum add the actual number, expected_sum adds the index
            curr_sum += nums[i]
            expected_sum += i
        # since we miss one number, we need to add one more length to the expected sum
        expected_sum += len(nums)
        return expected_sum - curr_sum
     
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        # use the formula of n * (n + 1) // 2 to get the sum of the continuous sum of array 
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        current_sum = sum(nums)

        return expected_sum - current_sum

# Hashset O(n) and O(n)
class Solution:
    def missingNumber(self, nums):
        # convert list to set and loop over to see which one is not in set()
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


# O(n) time complexity solution using Gauss' formula. O(1) space complexity.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of the first n natural numbers
        current_sum = sum(nums)

        # Use Gauss' formula to calculate the expected sum of the first n natural numbers
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2

        # The missing number is the difference between the expected sum and the current sum
        return expected_sum - current_sum
