# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

# Constraints:

# 1 <= n <= 231 - 1
 

# Follow up: If this function is called many times, how would you optimize it?


class Solution:
    def hammingWeight(self, n: int) -> int:
        # it works, but I should implement my own trick instead of using bin
        # binary_string = bin(n)[2:]
        # total_one = 0

        # for x in binary_string:
        #     if int(x) == 1:
        #         total_one += 1
        
        # return total_one

        count = 0
        while n:
            count += 1
            # looping to remove the last bit that is 1
            # n     = 1100
            # n - 1 = 1011
            # ---------------
            # n & (n - 1) = 1000
            n = n & (n - 1)
        
        return count 