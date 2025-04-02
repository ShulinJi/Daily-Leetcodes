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

        # Negating the numebrs, it works, but I cannot prove it 
        for num in nums:
            cur = abs(num)
            print("cur", cur)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]
            print(nums)

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate