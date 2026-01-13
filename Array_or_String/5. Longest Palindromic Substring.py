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

# SECOND ATTEMPT, O(n^2) and O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            # -2 because i and j is 1 index over the correct palindrome for both i and j after final iteration
            return j - i - 2 + 1

        ans = [0, 0]
        for i in range(len(s)):
            # first check case: expand from the centre with unique char at middle, ex: "caabaad"
            length = expand(i, i)
            if length > ans[1] - ans[0] + 1:
                middle = length // 2
                ans[0] = i - middle
                ans[1] = i + middle
            
            # now we check the case where no centre exists
            length = expand(i, i + 1)
            # "eccaaaaccf", i = 4 we have a palinrome, length 8, no middle, middle = 8//2 - 1, left = 1
            if length > ans[1] - ans[0] + 1:
                middle = length // 2 - 1
                ans[0] = i - middle
                ans[1] = i + middle + 1
        
        return  s[ans[0]: ans[1] + 1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # my own solution
        def expand(i, j):
        # i can be 0! but j cannot be len(s)
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 2 + 1
    
        ans = [0, 0]
        for i in range(len(s)):
            # test expand from single centre
            length = expand(i, i)
            if length > ans[1] - ans[0] + 1:
                middle = length // 2
                ans[0] = i - middle
                ans[1] = i + middle
            
            # test expand from 2 
            length = expand(i, i + 1)
            if length > ans[1] - ans[0] + 1:
                # length 4 but there is no middle, only plus on on each i and i + 1
                middle = length // 2 - 1
                ans[0] = i - middle
                ans[1] = i + 1 + middle
                    
        return s[ans[0]:ans[1] + 1]



# Editorial
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


# Brute-force just find all substring and check palindrome
        
