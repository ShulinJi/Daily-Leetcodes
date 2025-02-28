# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the string to words -> the array of same size
        words = s.split()
        if len(words) != len(pattern):
            return False

        # create two hashmaps to determine if they are mapped to each other
        # Need two maps b/c to avoid duplicate mapping, need to ensure unique one to one map
        # pattern: "abba", string: "dog dog dog dog"
        # In this case, if we only one map, we will map a -> dog and b -> dog, which is wrong, so we need to check both ways
        # that a -> dog and dog -> a to ensure the correctness
        hashmap_pattern_to_s = {}
        hashmap_s_to_pattern = {}
        for x in range(len(pattern)):
            # the case that we haven't met the mapping before, so we map each other
            if pattern[x] not in hashmap_pattern_to_s and words[x] not in hashmap_s_to_pattern:
                hashmap_pattern_to_s[pattern[x]] = words[x]
                hashmap_s_to_pattern[words[x]] = pattern[x]
                # if we have seen the word, then we check if the mapping is correct
            elif (hashmap_pattern_to_s.get(pattern[x]) != words[x]) or (hashmap_s_to_pattern.get(words[x]) != pattern[x]):
                return False
        
        return True