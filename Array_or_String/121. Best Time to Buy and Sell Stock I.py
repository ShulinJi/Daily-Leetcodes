# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# SECOND ATTEMPT O(n) and O(1), One Pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 4
        profit = 0

        # keep the cheapest buy, and traverse for the better profit

        # for each price, we first check if it is a smaller price, if it is, then we update
        # the min_price without considering the profit
        # for this, we can ensure that we will not calculate subtract min_price with previous price
        # because we are traversing to to the right and never go back to previous price after we update the min_price
        for price in prices:
            # it is safe to update the min because once we find a new min, everything after this min will be strictly 
            # better, like price - new_min > price - old_min
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price
        return profit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n*2) too slow
        # profit = 0
        # currentPrice = 0
        # for x in range(len(prices)):
        #     currentPrice = prices[x]
        #     maxSellPrice = max(prices[x:])
        #     maxProfit = max(0, maxSellPrice - currentPrice)
        #     profit = max(profit, maxProfit)
        # return profit

        # O(n) runtime
        min_price = float("inf")
        max_profit = 0 
        for price in prices:
            # we keep track the minimum price we have seen so far and this made sure
            if price < min_price:
                min_price = price
            # Use elif to ensure that we don't buy and sell on same day (only if or else, cannot both)
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
