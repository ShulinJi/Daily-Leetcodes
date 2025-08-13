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

# O(log(n)) time, O(1) space, binary search solution
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            # calculate the number of coins needed to complete mid rows
            # using the formula for the sum of the first k natural numbers: k * (k + 1) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            if curr > n:
                right = mid - 1
            else:
                left = mid + 1

        # when we exit the loop, right is the largest number such that right * (right + 1) // 2 <= n, so we return right b/c we 
        # want the maximum 
        return right

# O(1) time, O(1) space, mathematical solution
# This solution uses the quadratic formula to find the maximum number of complete rows
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Using the formula k(k + 1) <= 2n, we can rearrange it to find k
        # (k +0.5) ^ 2 - 0.25 <= 2n
        # k = (sqrt(2n + 0.25) - 0.5)
        return (int)((2 * n + 0.25)**0.5 - 0.5)

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
        