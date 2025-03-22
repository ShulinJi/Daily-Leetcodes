# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

# Sliding windows!!!!!!!!!!
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        # length for p string and s string
        np = len(p)
        ns = len(s)

        # two hashmap used to compare against each other
        s_map = {}
        p_map = {}

        returnList = []
        # populate the p map
        for char in p:
            if char in p_map:
                p_map[char] += 1
            else:
                p_map[char] = 1
        
        # sliding window that keeps the length of p string
        for i in range(ns):
            # add the element to the hashmap
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1
            
            # pop the entry if only 1 count or decrease count if count > 1
            if i >= np:
                if s_map[s[i - np]] == 1:
                    del s_map[s[i - np]]
                else:
                    s_map[s[i - np]] -= 1
            
            # check if updated map equals to the target map, if yes, then we have anagram
            if s_map == p_map:
                returnList.append(i - np + 1)
        
        return returnList