class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(num, n):
            # base condition when n = 0, the power 0 of a number is 1
            if n == 0:
                return 1
                
            # if the power is negative, then we calculate the total and then take its reciprocal
            if n < 0:
                return 1 / power(num, -1 * n)
                
            # we are doing power division by divide power by 2, we simply do x * x = x^2
            if n % 2 == 1:
                return num * power(num * num, (n - 1) // 2)
            else:
                return power(num * num, n // 2)

        return power(x, n)



# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
