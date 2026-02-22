# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# SECOND ATTEMPT
class Solution:
    def addBinary(self, a, b) -> str:
        # convert string to numbers and to binary
        a_bit = int(a, 2)
        b_bit = int(b, 2)

        while b_bit:
            # xor of 2 numbers equal to add two numbers without caring the carry bit
            # since xor is only 1 when bits are 0 and 1 or 1 and 0, 
            curr_sum = a_bit ^ b_bit

            # then we take care of carry bit by AND to find the 1 and 1 that result in 1 and we 
            # shift the position by 1 bc 01 + 01 = 10
            carry_bit = (a_bit & b_bit) << 1

            # then we keep iterating the process until there is no carrying bit to process
            a_bit, b_bit = curr_sum, carry_bit
        
        # bin(a_bit) convert it from int to binary with 0b at the start
        return bin(a_bit)[2:]

class Solution:
    def addBinary(self, a, b) -> str:
        # convert number to binary form
        x, y = int(a, 2), int(b, 2)

        while y:
            # Use XOR: result from XOR, only 0/1 or 1/0 can result 1, others like 0/0, 1/1 are all 0
            # So the results are adding up but without any carrying bit (ignore any 1+1 that result carry bit)
            answer = x ^ y

            # Use & which is AND so that only 1/1 can be 1, which represents the AND logic, and only 1/1 results in carry bit
            # After we use AND, we get the carry bit, then we shift it to left 1 bit b/c the carrying bit needs to be moved forward like 01 + 01 = 10
            carry = (x & y) << 1
            # Then we keep adding the carrying bits withg partial sum from XOR until there is no more carry bit after the XOR(partial sum) operation
            x, y = answer, carry
        
        # x = 13
        # bin(x) → '0b1101'
        # bin(x)[2:] → '1101'
        return bin(x)[2:]
