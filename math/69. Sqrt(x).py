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
