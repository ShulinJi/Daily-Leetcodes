# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # mapp all the elements with numbers of appearances
        char_freq = {}
        for x in s:
            if x in char_freq:
                char_freq[x] += 1
            else:
                char_freq[x] = 1
        
        maxLength = 0
        # if there is odd number of appearance, we can form (bacab), else only (baab)
        haveSingleCharacter = False
        for freq in (char_freq.values()):
            # count number of pairs we can get
            # if we have a pair, then we add 2 to the total length
            if not haveSingleCharacter:
                if freq % 2:
                    haveSingleCharacter = True
            num_of_pairs = freq // 2
            # update total length
            maxLength += num_of_pairs * 2
        
        return maxLength if not haveSingleCharacter else maxLength + 1
