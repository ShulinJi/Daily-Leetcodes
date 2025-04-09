# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# DP Problems:
# I know I'm working with DP when I can define a recursive algorithm 
# where the answer at a current step is some function of previous or future steps and the function only requires you to call the function at different values.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # top-down approach

        # each index means the minmum number of coins needed to achieve it 
        dp = [float("inf")] * (amount + 1)
        # initial state 0 dollar with 0 coins needed
        dp[0] = 0

        # loop through initial coins 
        for coin in coins:
            # first start with 0, then first loop populate the 1, 2, 5 with 1, and then start with 1, begin to add 1 coin to each amount increased
            # result in a 12 in amount 12, and then we begin to start with 2 and update the new minimum and then 5 with the minimum
            # if the number cannot be reached, it will stay as float(inf) as it won't be updated!
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
