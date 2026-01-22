# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# SECOND ATTEMPT
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(logn)
        left = 0
        right = len(nums) - 1
        left_bound = -1
        right_bound = -1

        # try to find left bound
        # when we find the target, we update the bound
        # it is guranteed to converged because of the condition
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
                left_bound = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # find right bound
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
                right_bound = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [left_bound, right_bound]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        leftmost = -1
        rightmost = -1
        # find the leftmost occurence for the target
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # when we find the match, we don't break, but to shrink the range again to look for potential earlier match
                leftmost = mid
                # right = mid - 1 becuase the condition left <= right, we don't want to risk the potential of infinite loop by increasing left!
                right = mid - 1
        
        # start a new binary search to find the rightmsot occurance of the number
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # same reason as the last one 
                rightmost = mid
                left = mid + 1
        
        return [leftmost, rightmost]
