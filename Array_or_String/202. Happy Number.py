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










        # seen = set()
        # while n != 1 and n not in seen:
        #     string = str(n)
        #     total = 0
        #     for x in string:
        #         total += (int(x)) ** 2
            
        #     if total == 1:
        #         return True
        #     seen.add(n)
        #     n = total
        
        # return n == 1