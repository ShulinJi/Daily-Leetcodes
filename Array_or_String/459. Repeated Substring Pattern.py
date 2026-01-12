# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

# SECOND ATTEMPT
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # we need n // 2 + 1 because if it is only n//2, ex. len(s) == 4, then n // 2 = 2, then (1, 2) will only check 1,
        # then we missed the case of abab where we need to check 2 as well
        for i in range(1, n // 2 + 1):
            # if n can be divisible by i, it means we have a chance of forming it
            if n % i == 0:
                # n // i is the number of repetion
                new_string = s[:i] * (n // i)
                if new_string == s:
                    return True
        
        return False
     
 # O(n) and O(n), advanced approach
 class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        if s in t[1:-1]:
            return True
        return False

# O(n * sqrt(n)) time | O(1) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # check for all possible lengths of substring from 1 to n/2, n// 2 + 1 because a substring can't be longer than n/2 (in order to repeat at least twice)
        for i in range(1, n // 2 + 1):
            # if n is divisible by i, then we can form a new string by repeating the substring of length i, n // i times
            if n % i == 0:
                # form the new string by repeating the substring of length i, n // i times
                new_string = s[:i] * (n // i)
                if new_string == s:
                    return True
        
        return False


