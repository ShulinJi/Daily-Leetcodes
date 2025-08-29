# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

# time complexity: O((T+P) * 2 ^(T + P)) where S is the length of string and T is the length of pattern
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if we exhausted the pattern but the text is still not empty, then not match false
        if not p:
            return not s
        
        # first char matches if s is not empty and the first char of p is either '.' or matches the first char of s
        # counter-example: s = "a", p = "b", without checking first char of s, it would return True
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == "*":
            # 2 cases, first is to skip the pattern a*, or we keep matching aaaa with a* (consume)
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            # move to next char in both s and p if first char matches
            return first_match and self.isMatch(s[1:], p[1:])