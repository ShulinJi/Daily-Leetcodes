# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1


# # O(sqrt(n)) time, O(1) space
class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = n
        stairs = 0
        if coins <= 1:
            return coins

        # we can use a for loop to iterate through the number of rows
        # and subtract the number of coins needed for each row
        for i in range(1, n + 1):
            # if the number of coins is less than the number of coins needed for the next row (exhausted all coins),
            # we return the number of complete rows
            if stairs != 0 and coins < stairs + 1:
                return stairs
            coins -= i
            stairs += 1
        