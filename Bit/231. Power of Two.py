# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

# SECOND ATTEMPT
# O(1) and O(1), another approach to check if it is power of 2, bc number that are power of 2 has only 1 in all the bits, such as 1000, 100, 10000
# so when we n - 1, we flip all the bits 1000 - 1 is 0111, so the AND operator will always give us 0!
class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return True if n & (n - 1) == 0 else False

# O(1) time | O(1) space with bit manipulation
class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # 2's complement
        # if n is a power of two, it has exactly one bit set in its binary representation, then -n = ~n + 1 (which flips all bits of n and adds 1,
        # and only the number that is power of 2 will result in flipping all bits to 1 except the lowest set bit 0000100 => 1111100)
        # thus, n & -n will give us the value of the lowest set bit, 0000100 and 1111100 will result in 0000100, which is equal to n itself
        # this means that if n is a power of two, n & -n will equal n itself 
        # so n & -n will leave only the lowest set bit of n, if n is a power of two, it should be equal to n itself
        return n & (-n) == n

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                return False
        
        return True
