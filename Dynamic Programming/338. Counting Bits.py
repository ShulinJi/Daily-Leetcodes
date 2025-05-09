# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


class Solution:
    def countBits(self, n: int) -> List[int]:
        # simple bit removal method O(nlogn)
        # For each integer x, in the worst case, we need to perform O(logn) operations, 
        # since the number of bits in x equals to logx+1 and all the bits can be equal to 1
        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1 # zeroing out the least significant nonzero bit
                count += 1
            return count
            
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
    
        return ans                                


class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) runtime, and O(1) space complexity if output array doesn't count 
        # For each integer x, in the range 1 to n, we need to perform a constant number of operations which does not depend on the number of bits in x
        # The outer loop defines the boundaries of each block: 1, 2, 4, 8, 16, ...
        # These are powers of 2: they mark where the number of bits increases by 1.
        # The inner loop fills in the values within each block, based on values from the previous block.
        ans = [0] * (n + 1)
        x = 0
        b = 1
        
        # [0, b) is calculated
        # P(x+b)=P(x)+1,b=2 m>x
        # since 2^0 = 1(0), 2^1 = 2(10), 2^2 = 4(100), 2^3 = 8 (1000), every time we move by 1 bit, we add one more 
        # new_num = old_num + b, old_num = 3 → 0b011, b = 4 = 2^2, new_num = 3 + 4 = 7 → 0b111, popcount(7) = popcount(3) + 1 = 2 + 1 = 3
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0 # reset x
            b <<= 1 # b = 2b
            
        return ans  