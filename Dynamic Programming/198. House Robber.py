# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down approach
        # we start from the end of the house
#         how did you arrive at the last house? either
# A: you robbed the previous house (can't rob current house)
# B: you robbed the second previous house (can rob current house)

# and you keep repeating this branching logic (choice A or B) until the base case where you're at the first house.
        n = len(nums)
        dp = [0] * (n + 1)

        # we haven't made any choice b/c we are not in any house, just like we skipped all the houses
        dp[n] = 0
        # “What is the maximum amount of money you can rob starting from house n - 1 (the last house), given that you haven’t made any choices yet?”
        dp[n - 1] = nums[n - 1]

        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        
        return dp[0]