# 205. Isomorphic Strings
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
 
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # one kind of character in s maps to only one character in t, so whenver we see a character again, we need to check if it maps to the same character in t
        # two hashmaps used to map each character in string to another character in another string
        s_to_t = {}
        t_to_s = {}

        # this means char1 in s, and char2 in t, and loop one by one
        for char1, char2 in zip(s, t):
            # first case where we have never met the character, we map it to our hashmap
            if char1 not in s_to_t and char2 not in t_to_s:
                s_to_t[char1] = char2
                t_to_s[char2] = char1
            # second case, we have seen the map before, but now the characters are not the same
            # ex. p -> a before, and then we have p -> b, a != b, which would be this case
            # one same character cannot be mapped to different characters

            # use get() to avoid key error because char1 or char2 may not be in the hashmap yet
            elif s_to_t.get(char1) != char2 or t_to_s.get(char2) != char1:
                return False
            
        return True