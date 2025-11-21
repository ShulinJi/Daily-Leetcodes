
# O(n) time | O(1) space since the hashmap will have at most 26 keys for aplhabet letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_s = {}
        for x in s:
            if x in char_s:
                char_s[x] += 1
            else:
                char_s[x] = 1
        
        for x in t:
            if x in char_s:
                char_s[x] -= 1
        for x in char_s.values():
            if x != 0:
                return False
        
        return True
        
        # return sorted(s) == sorted(t)


# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
