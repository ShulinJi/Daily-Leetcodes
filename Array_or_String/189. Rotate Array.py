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


# Brute Force, O(n x k), O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # O(n x k) because k rotation for O(n) rotating once, O(1)
        # speed up rotation
        k = k % len(nums)
        
        # number of rotating to the right by 1 required
        for i in range(k):
            # the first number needs to be changed with last one since rotating to the right
            previous = nums[-1]
            for j in range(len(nums)):
                # each time, we fill out the array, previous is the the value we should have at the current place
                # ex. [1,2,3,4,5,6,7], then 1 becomes 7 ,previous becomes 1, then next iter: 2 becomes previous 1 ,and previous becomes 2, then next iter and so on
                nums[j], previous = previous, nums[j]
        
        return nums

# O(n) and O(n), using extra array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            # use (i + k) % len(nums) to find the position after the rotation
            ans[(i + k) % len(nums)] = nums[i]
        
        nums[:] = ans
        return nums



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

        
