# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

# valleys and peaks approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) and O(1) 
        # we iteratively find the valleys and peaks 
        profit = 0
        i = 0

        # after we find valley and peak
        while i < len(prices):
            # valley is a low point where it's price is smaller than next one
            while i < len(prices) - 1 and prices[i] > prices[i + 1]:
                i += 1
            valley = prices[i]

            # peak is the local high point where it's price is higher, so when it is smaller, we move forward to find next
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
            peak = prices[i]
            profit += peak - valley
            
            i += 1

        return profit

# SECOND ATTEMPT
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 10 ** 4
        # if we see a higher price we sell and then buy at the same time to avoid missing the case of consecitive buy sell
        # if we see a low price, we update the min
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit += price - min_price
                min_price = price
        
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) runtime and greedy algorithm
        if len(prices) < 2:
            return 0

        total_profit = 0
        # Since we can buy and sell on same day, then we only need to see if next value is greater than today, if so, we just buy and sell
        for x in range(1, len(prices)):
            if prices[x] > prices[x - 1]:
                total_profit += prices[x] - prices[x - 1]

        return total_profit
