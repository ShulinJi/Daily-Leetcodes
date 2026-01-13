# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# SECOND ATTEMPT O(n) and O(1), Two Pointer
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointer with j <= i, always write to j to override the array based on the requirement
        # start with 1 because we need to check th front one
        i = 1
        j = 1
        # count also starts at one because we have traversed through the first element
        count = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                # if count is bigger than 2, then we simply ignore it and don't override the array (skipped)
                # and the extra ones will be override in future loops by num[j] = num[i] since j < i always
                if count > 2:
                    i += 1
                    continue
            else:
                # we reset the count back to one since we start at a new element
                count = 1
            # we keep overriding the array such that each element can only appear up to two times
            nums[j] = nums[i]
            i += 1
            j += 1
        
        return j

# Instead of override, we pop the unwanted element!
# same O(n) and O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Check for edge case where list is empty
        if not nums:
            return 0

        # Pointer for current index in the list
        i = 1
        # Count of the current element occurrences
        count = 1

        # Iterate through the list starting from the second element
        while i < len(nums):
            # Check if the current element is same as the previous one
            if nums[i] == nums[i - 1]:
                # Increment count for the current element
                count += 1
                # If count exceeds 2, remove the current element
                if count > 2:
                    nums.pop(i)
                    i -= 1
                    count -= 1
            else:
                # Reset count for new element
                count = 1
            # Move to the next element
            i += 1

        # Return the new list length
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ### if length is smaller than 2, we simply return its length
        if len(nums) <= 2:
            return len(nums)

        ### 2 pointers, i is for traversing through the nums and j points at the place where we need to overwrite after meet of 2 values (count)
        i = 1
        j = 1
        count = 1
        while i < len(nums):
            # check to see if current number is same as last one
            if nums[i] == nums[i - 1]:
                # if so, we increment the count
                count += 1
                # if count is bigger than 2, we don't update and move to the next until we see a different value
                if count > 2:
                    i += 1
                    continue
            else:
                # we reset the counter to 1 if we see a different value
                count = 1
            # we keep overwrite the j if the counter is <= 2 or we see a new value(count == 0)
            nums[j] = nums[i]
            # we increment both pointer after each overwrite
            i += 1
            j += 1

        return j



        ### Brute Force, we remove the extra element whenever we see an extra
        ### O(N^2) runtime and O(1) space since in-place
        if len(nums) <= 2:
            return len(nums)
        
        i = 1
        count = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    count -= 1
                    i -= 1
            else:
                count = 1
            i += 1
        
        return len(nums)
