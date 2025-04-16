# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

class Solution:
    def reorganizeString(self, s: str) -> str:
        # O(n) and O(n) time and space complexity
        char_count = {}
        for x in s:
            if x in char_count:
                char_count[x] += 1
            else:
                char_count[x] = 1
        
        # find the largest frequency of char
        max_count = 0
        max_char = 0
        for char, count in char_count.items():
            if count > max_count:
                max_count = count
                max_char = char

        # if over half the elements are same, it means we cannot find a possible solution!
        if max_count > (len(s) + 1) // 2:
            return ""
        ans = [""] * len(s)
        index = 0

        # then we first populate the longest frequency characters by populating the even index
        while char_count[max_char] != 0:
            ans[index] = max_char
            index += 2
            char_count[max_char] -= 1

        # then we populate the rest of them
        for char, count in char_count.items():
            while count > 0:
                # if we exceed the len, then we start from index 1 to fill the odd index
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1
        
        return "".join(ans)