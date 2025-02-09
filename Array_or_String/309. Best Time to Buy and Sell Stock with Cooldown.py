# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)



# Notice the order of operations:

# (A) Save the Old sold:
# We first save the current value of sold (which was computed in the previous iteration) into pre_sold.

# (B) Update sold:
# We then compute sold = held + price, which means “if I sell the stock I was holding today, what would my profit be?”

# (C) Update held:
# When deciding whether to continue holding a stock or to buy one, the algorithm uses:

# python
# Copy
# held = max(held, reset - price)
# This means you can only buy a stock using the reset state, not using the newly computed sold state from today.

# (D) Update reset:
# Finally, we update reset using:

# python
# Copy
# reset = max(reset, pre_sold)
# This update takes the best profit from the previous day’s sale (pre_sold) and makes it available for future buying decisions. Importantly, the sold value from the current day is not used in the decision to buy a stock today.

# How This Enforces the Cooldown
# After a Sale:
# Suppose you sell a stock on day i. This sale updates the sold variable with held + price. However, notice that when you get to the buying decision on day i, you compute:

# python
# Copy
# held = max(held, reset - price)
# At this point, the reset variable has not yet been updated with today's sale because its update happens after the buying decision. Thus, even if you sold a stock on day i, you cannot use that profit immediately (i.e., in the same iteration) to buy another stock. You have to wait until the next day when reset gets updated with the profit from sold.

# Cooldown Period:
# The update reset = max(reset, pre_sold) effectively transfers the profit from a sale to the reset state only for the next day. This means:

# On day i: You sell a stock and update sold, but the opportunity to buy is still based on the reset value from day i-1.
# On day i+1: Now reset may have been updated (from the sale on day i), and that profit becomes available for buying. Thus, you’re forced to wait one full day after selling before that profit can be used to purchase another stock.