# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


class Solution:
    def tribonacci(self, n: int) -> int:
        # bottom-up approach
        if n < 3:
            return 0 if not n else 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        
        return dp[n]


# top-down without memorization, exceed time limit
class Solution:
    def tribonacci(self, n: int) -> int:
        # without memorization, exceed time limit!
        # we are doing repetitve work for same operation, simply naive recursion
        # Need to memorize the answer!
        # time complexity would be O(3^n) !
        def find_tribonacci(n):
            if n < 3:
                return 0 if not n else 1

            ans = find_tribonacci(n - 1) + find_tribonacci(n - 2) + find_tribonacci(n - 3)
            return ans

        return find_tribonacci(n)


# correct top-down, recursion with memorization
# O(n) and O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}
        def find_tribonacci(n):
            if n < 3:
                return 0 if not n else 1

            # memorize the operation so that we don't execute the same operation more than once
            # b/c we are solving sub-optimal problems that each subproblem only have one optimal solution
            if n in mem:
                return mem[n]

            ans = find_tribonacci(n - 1) + find_tribonacci(n - 2) + find_tribonacci(n - 3)
            mem[n] = ans

            return ans

        return find_tribonacci(n)


# even better, find the pattern and O(n) time, O(1) space complexity
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c

        
