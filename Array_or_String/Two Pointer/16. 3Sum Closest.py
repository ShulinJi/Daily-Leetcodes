# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# second attempt, O(n^2) time complexity, O(logn) space complexity due to sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_diff = float("inf")

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - current_sum)
                if diff < closest_diff:
                    ans = current_sum
                    closest_diff = diff
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return ans
        return ans


# O(n^2)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        returnSum = None
        closestDiff = float("inf")

        # Two pointers need to be sorted!
        nums = sorted(nums)

        #  first is find a number and do a two sum using two pointers
        for x in range(len(nums)):
            # find a number and skip the duplicates
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = x + 1
            j = len(nums) - 1

            # Use two pointers to find the smallest diff for current combinations
            while i < j:
                currentSum = nums[x] + nums[i] + nums[j]
                diff = abs(currentSum - target)
                if diff < closestDiff:
                    closestDiff = diff
                    returnSum = currentSum
                if currentSum < target:
                    i += 1  # Increase the sum by moving i to the right
                elif currentSum > target:
                    j -= 1  # Decrease the sum by moving j to the left
                else:
                    return returnSum  # If exactly equal to target, return immediately

        return returnSum
