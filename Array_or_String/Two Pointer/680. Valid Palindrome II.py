# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Check normal palidrome string
        def checkPalindrome(left, right, s):
            while left < right:
                while not s[left].isalnum():
                    left += 1
                
                while not s[right].isalnum():
                    right -= 1
                
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        # whenever we find the mismatch, we test two cases that could happen, delete left or delete right
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(i + 1, j, s) or checkPalindrome(i, j - 1, s)
            i += 1
            j -= 1

        return True




# follow up: if we change the question to be up to k modifications:
# recursion with memorization
# O(n² * k)
class Solution:
    def validPalindromeK(self, s: str, k: int) -> bool:
        memo = {}

        def helper(left, right, k):
            if (left, right, k) in memo:
                return memo[(left, right, k)]

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if k == 0:
                        memo[(left, right, k)] = False
                        return False
                    res = helper(left + 1, right, k - 1) or helper(left, right - 1, k - 1)
                    memo[(left, right, k)] = res
                    return res

            memo[(left, right, k)] = True
            return True

        return helper(0, len(s) - 1, k)