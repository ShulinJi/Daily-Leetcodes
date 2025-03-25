# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

# Constraints:

# 1 <= n <= 1690

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = []  # min-heap to store and retrieve the smallest ugly number
        seen_numbers = set()  # set to avoid duplicates
        prime_factors = [2, 3, 5]  # factors for generating new ugly numbers

        heapq.heappush(min_heap, 1)
        seen_numbers.add(1)

        current_ugly = 1
        for _ in range(n):
            current_ugly = heapq.heappop(min_heap)  # get the smallest number

            # generate and push the next ugly numbers
            for prime in prime_factors:
                next_ugly = current_ugly * prime
                if next_ugly not in seen_numbers:  # avoid duplicates
                    heapq.heappush(min_heap, next_ugly)
                    seen_numbers.add(next_ugly)

        return current_ugly  # return the nth ugly number