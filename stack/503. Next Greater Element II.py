# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
 

# Constraints:

# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109

# O(n) time complexity solution using a stack. O(n) space complexity.
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        # Traverse the array backwards twice to simulate circular behavior
        for i in range(2 * n - 1, -1, -1):
            # Maintain the stack to find the next greater element
            # Pop elements from the stack that are less than or equal to the current element because they cannot be the next greater element
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                res[i % n] = nums[stack[-1]]
            stack.append(i % n)
        
        return res