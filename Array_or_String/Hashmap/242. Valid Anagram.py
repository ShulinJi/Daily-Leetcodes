
# O(n) time | O(1) space since the hashmap will have at most 26 keys for aplhabet letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length is not the same, and they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # count occurence of s and record in hashmap
        char_s = {}
        for x in s:
            if x in char_s:
                char_s[x] += 1
            else:
                char_s[x] = 1
        
        # then traverse through t, then minus the count in hashmap when seeing the same character
        for x in t:
            if x in char_s:
                char_s[x] -= 1

        # if there is any character with count not 0, then they cannot be anagrams
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
