# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

# O(logn) and O(1)
# SECOND ATTEMPT
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # if right side is even, 
            right_side_even = (right - mid) % 2 == 0
            # because we have only one single element and others are all pairs, then it means we always haveodd number of elements in the nums array, then [1,1,2,2,3], if mid == mid + 1, single element is at right side, [1,2,2,3,3], if mid == mid - 1, single element is at left side
            if nums[mid] == nums[mid + 1]:
                # if right side is even, then it means, after we take the mid + 1 away, the rest is odd, then the answer is on the right side
                if right_side_even:
                    left = mid + 2
                else:
                    right = mid - 1

            # if right side is even and mid == mid - 1, then the answer is on left side because right side is even, there cannot be any single element, right = mid - 2 b/c we skipped the pair 2 element at a time
            elif nums[mid] == nums[mid - 1]:
                if right_side_even:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]
        
        return nums[left]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # O(logn) and O(1)
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            right_half_even = (high - mid) % 2 == 0
            
            if nums[mid] == nums[mid + 1]:
                # the single number is at the right half
                # if right half is even, then we minus the duplicate one with nums[mid], then right half will have odd number of numebrs
                # it means the single one will be at the right half, then we skip the current duplicate by skip mid and mid + 1
                if right_half_even:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid - 1]:
                # then single number is at the left half
                if right_half_even:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                low = mid
                break

        return nums[low]