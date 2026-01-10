# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

# SECOND ATTEMPT
class Solution:
    def isHappy(self, n: int) -> bool:
        # O(logn) and O(logn)
        seen = set()

        # we keep iterating and until we see 1 or we see a cycle(already in hashset)
        while n != 1:
            if n in seen:
                return False
            else:
                seen.add(n)
            n_str = str(n)
            new_num = 0
            # O(logn) dominating part
            for digit in n_str:
                new_num += int(digit) ** 2
            n = new_num

        return True

# Floyd's Cycle-Finding Algorithm
# O(logn) and O(1) with two pointer
# if they have a cycle, it means that it's false
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit**2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)

            new_n = 0
            n = str(n)
            for x in n:
                new_n += int(x) ** 2
            n = new_n
        
        return n == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        # the set that is used to detect a cycle (seen the number before)
        seen = set()
        # compute the number until we reach 1 or we detect a cycle!
        while n != 1 and n not in seen:
            seen.add(n)

            new_n = 0
            n = str(n)
            for x in n:
                new_n += int(x) ** 2
            n = new_n
        
        # check to see if the number is 1, if yes -> happy
        return n == 1
