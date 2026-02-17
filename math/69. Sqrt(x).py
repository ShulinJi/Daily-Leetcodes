
# SECOND ATTEMPT
# O(logn) and O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        # use binary search to find the closest number to the power of 2
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # we use left - 1 or right because when we terminate the condition is left > right = right + 1
        return right


class Solution:
    def mySqrt(self, x: int) -> int:
        # O(log(N))
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            # we keep the desired number between left and right since x // 2 is alawys bigger than sqrt(x) when x > 2
            # Then we shrink down the window by checking the pivot point
            # pivot is the middle point of left and right
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                # if we find the number that is exactly the sqrt of the integer
                return pivot

        return right



# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
