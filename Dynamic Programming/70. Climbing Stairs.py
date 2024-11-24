class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute Force we return 1 whenver there is a approach that reaches the target n, else we don't count it.
        # O(2^n)
        # def climb_stairs(i, n):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     return climb_stairs(i + 1, n) + climb_stairs(i + 2, n)

        # return climb_stairs(0, n)

        # Dynamic Programming (DP)
        # As we can see this problem can be broken into subproblems, and it contains the optimal substructure property i.e. its optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic programming to solve this problem.
        # O(n) runtime and O(n) space
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
