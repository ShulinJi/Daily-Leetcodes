# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30

# O(n) time complexity, O(n) space complexity
# Approach 2: Bottom-Up Approach using Tabulation
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        # Create a list to store Fibonacci numbers up to n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        # Fill the list using the Fibonacci relation
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# O(n) time complexity, O(n) space complexity
# Approach 3: Top-Down Approach using Memoization
class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]