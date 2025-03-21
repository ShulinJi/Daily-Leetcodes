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


class Solution:
    def isHappy(self, n: int) -> bool:
        # we first use a set() to record the numbers we have seen since we check if ... in set often
        # We use this set to detect the cycle (we have seen the number) 
        seen = set()
        # we break when we see 1 or a cycle being detected
        while n != 1 and n not in seen:
            # we add current number to set
            seen.add(n)

            # we compute the new n by convert to string and loop over
            new_n = 0
            n = str(n)
            for x in n:
                new_n += int(x) ** 2
            n = new_n
        
        return n == 1



class Solution:
    def isHappy(self, n: int) -> bool:
     # the number would either stuck in a cycle or reach 1
        seen = set()
        while n != 1 and n not in seen:
            string = str(n)

         # calculate the total of the current number
            total = 0
            for x in string:
                total += (int(x)) ** 2
            
            if total == 1:
                return True
             # use set to detect duplicates or cycles
            seen.add(n)
            n = total
        
        return n == 1
