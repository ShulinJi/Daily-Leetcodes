# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104
 

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mimd] == target:
                return True
            
            # check if binary search could apply in this case
            binary_search_helpful = self.binarySearchHelpful(nums, start, nums[mid])
            # binary search does not work, we move start to the right, safe move even though not efficient
            if not binary_search_helpful:
                start += 1
                continue

            # if mid is in the first half of sorted array
            mid_in_first_half = self.inFirstHalf(nums, start, nums[mid])
            # if target is in the first half of sorted array
            target_in_first_half = self.inFirstHalf(nums, start, target)

            # ^ operator XOR: only true when only one of them is true
            # it means mid and target will be at different arrays since if mid is true => in first array, then to satisfy condition,
            # target needs to be at second sorted array
            if mid_in_first_half ^ target_in_first_half:
                # if mid is in first half, then target is in second half, which means we can safely prune the first half
                if mid_in_first_half:
                    # prune the first half
                    start = mid + 1
                else:
                    # prune the second half
                    end = mid - 1
            # if on the same side of the array, we do the normal binary search because the comparison ums[mid] < target is valid in sorted order!
            # then the other half that don't have target and mid will be discarded due to binary search
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


    # used to check if the number is in the first half of the sorted array
    def inFirstHalf(self, nums, start, element)
        return nums[start] <= element
    
    # check if binary search is helpful
    # if nums[start] == nums[mid], we cannot use binary search because it could be not sorted, then binary search would break
    def binarySearchHelpful(self, nums, start, element):
        return nums[start] != element
