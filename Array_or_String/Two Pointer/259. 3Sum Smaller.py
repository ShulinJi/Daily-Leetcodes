# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example 1:
# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]

# Example 2:
# Input: nums = [], target = 0
# Output: 0

# Example 3:
# Input: nums = [0], target = 0
# Output: 0


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # O(n^2) time and O(1) space if doesn't count the space for sorting, if count, it will be O(logn)
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            # first find the complement
            complement = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            #  takes O(n) to find the satisfied comb
            while left < right:
                # if the condition satisfy, it means that there are (right - left) many comb between them that satisfy the
                # the condition because the array is sorted, if the current right is good, then any right smaller than
                # current index would also work, it is like we move the right pointer to the left and that's interval 
                # satisfy the the condition
                if nums[left] + nums[right] < complement:
                    ans += right - left
                    # we only move the left because the current situation is smaller
                    left += 1
                else:
                    # we try to move right pointer to make it smaller to satify the condition
                    right -= 1
        
        return ans
