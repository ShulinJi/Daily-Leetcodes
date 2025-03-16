# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(N^2) runtime, and O(logn) to O(N) space
        returnList = []
        nums.sort()
        for i in range(len(nums)):
            # ignore the duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            complement = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # the sum is bigger than complement, decrease right
                if nums[left] + nums[right] > complement:
                    right -= 1
                elif nums[left] + nums[right] < complement:
                    left += 1
                # we find the match
                else:
                    returnList.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # we skip the duplicates here
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return returnList
        