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

# SECOND ATTEMPT

# even better with only 1 pass!
# O(n) and O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0

        # Loop over characters in the string
        for c in s:
            # If set contains the character, match found, we found a pair, add 2 to ans
            if c in character_set:
                character_set.remove(c)
                # Add the two occurrences to our palindrome
                res += 2
            else:
                # Add the character to the set
                character_set.add(c)

        # If any character remains, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if character_set:
            res += 1

        return res

# O(n) and O(1) solution because only 52 characters
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # frequency hashmap of the characters
        freq = Counter(s)
        
        # hasSinglechar used to check if the string has a unpaired character (single)
        # single character can be put the the middle of the palindrome +1 in the length
        hasSinglechar = False
        pairs = 0
        for count in freq.values():
            # check if the string has single char
            if not hasSinglechar:
                if count % 2:
                    hasSinglechar = True
            # add the number of pairs to total count
            pairs += count // 2
        
        # if has single characters, we can +1 at the middle after all pairs of char
        # ex. we can go from "aabb" to "aacbb"
        return (pairs * 2) if not hasSinglechar else (pairs * 2 + 1)
            



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
