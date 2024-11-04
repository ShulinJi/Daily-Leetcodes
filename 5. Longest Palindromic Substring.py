class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # because we stop when it is not a palindrome, so we need to subtract by 1 (left - right + 1 - 2)
            return right - left - 1

      
        # we expand from the centre
        ans = [0, 0]
        for i in range(len(s)):
            # if the palindrome length is odd, it means that it starts at single element
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                # distance from the expand centre
                dist = odd_length // 2
                ans = [i - dist, i + dist]
            
            # if the palindrome length is even, it means that it starts at a pair
            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                # distance from the expand centre, i is the front one in the pair 
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i: j + 1]


# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Brute-force just find all substring and check palindrome
        
