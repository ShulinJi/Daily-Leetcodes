# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    # O(n) runtime, O(1) space
    # Reverse method
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)



        ### O(n) runtime and O(n) extra space
        # since every whole cycle doesn't change the order, we only need the module
        rotate_times = k % len(nums)
        # the numbers that are needed to move to front
        move_to_front = nums[len(nums) - rotate_times:]
        # numbers need to stay
        rest = nums[:len(nums) - rotate_times]

        # combine them
        move_to_front.extend(rest)
        nums[:] = move_to_front
        return 

        