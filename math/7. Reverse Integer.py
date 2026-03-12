# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        # O(log(x)) because we are dividing by 0 each time
        # leave the sign to avoid the exception of negative numbers
        sign = 1 if x >= 0 else -1
        reverse = 0
        # we use abs value to use div mod
        x = abs(x)

        while x:
            # 123, divmod(123, 10) is x = 12, mod = 3
            x, mod = divmod(x, 10)
            # then we keep doing the mod and it will form the reversed number
            reverse = reverse * 10 + mod

            # check for the negative bound
            if reverse > 2**31 and not sign:
                return 0
            # check for the positive bound
            if reverse > 2**31 - 1 and sign:
                return 0
            
            
        return sign * reverse
