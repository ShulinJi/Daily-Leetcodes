# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?

#O(n) time and O(1) space by negating the numbers
# but this modifies the input array even though we restore it at the end
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Negating the numebrs while traversing the array
        # when we see a negative number again, that is the duplicate becuase all numbers are in the range 1 to n and if we see a negative number again, 
        # it means we have seen that index before, which means that number is duplicate
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] *= -1

        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return duplicate

# O(n) time and O(1) space using Floyd's Tortoise and Hare (Cycle Detection)
# the problem forms a cycle because there is a duplicate number that points to the same index so that when 
# we traverse the array using the values as indices, we will jump to the same index twice, forming a cycle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) time and O(1) space using Floyd's Tortoise and Hare (Cycle Detection)
        # reduce problem to 142
        # start at the list
        slow = nums[0]
        fast = nums[0]

        # find the cycle, slow moves one at a time, fast moves at two at a time
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # then we find the start of the cycle
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow