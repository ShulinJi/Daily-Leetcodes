# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# To sum up, there are 3 possible cases after comparing target with nums[mid]:

# Case 1. If nums[mid] = target, which denotes that we have found target, return mid as its index.

# Case 2. If nums[mid] >= nums[left]. It implies that the left subarray nums[left ~ mid] is sorted. We can determine whether to proceed with this subarray by comparing target with the boundary elements:

# If nums[left] <= target and target < nums[mid], it suggests that the sorted left half might include target while the other half does not contain target. Consequently, we focus on the left half for further steps.
# Otherwise, the left half is guaranteed not to contain target, and we will move on to the right half.

# Case 3. If nums[mid] < nums[left], it implies that the left subarray is rotated and the right subarray nums[mid ~ right] is sorted. Therefore, we can determine whether to proceed with the right subarray by comparing the target with its boundary elements:

# If nums[mid] < target and target < nums[right], it implies that the sorted right half might contain target. As a result, we will move on with the right half.
# Otherwise, the right half is guaranteed not to contain target, and we will move on to the left half.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            # left side of mid is sorted 
            if nums[low] <= nums[mid]:
                # left side is sorted, and target is within the range of low and mid, truncate the right side
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    # otherwise, we truncate the left side since target is bigger than the mid
                    low = mid + 1
            else:
                # right side of mid is sorted and target is inside right side, we truncate the left side
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    # target is bigger than the big, and right side is sorted, so it has to be at the left side, we truncate the right side
                    high = mid - 1
        
        return -1