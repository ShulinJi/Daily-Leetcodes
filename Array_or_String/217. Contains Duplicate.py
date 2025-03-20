# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Can sort and compare nums[i] == nums[i - 1], O(nlogn) & O(1)

        # O(n) & O(n)
        newset = set()
        for x in nums:
            if x in newset:
                return True
            else:
                newset.add(x)
        
        return False