# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

 

# Example 1:

# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
# Example 2:

# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".
 

# Constraints:

# 1 <= word.length <= 20
# word consists of only lowercase English letters.
# 1 <= abbr.length <= 10
# abbr consists of lowercase English letters and digits.
# All the integers in abbr will fit in a 32-bit integer.

# SECOND ATTEMPT
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0
        p2 = 0

        while p1 < len(word) and p2 < len(abbr):
            # if in abbr it is char, then they must match
            if abbr[p2].isalpha():
                # if they match, we check the next index of both string
                if abbr[p2] == word[p1]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
            else:
                # now we are in else, it means we have a number, then no leading zero
                if abbr[p2] == "0":
                    return False
                
                # we form the number to see how many characters we need to skip
                num = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    num = num * 10 + int(abbr[p2])
                    p2 += 1
                # we need to skip this many characters for p1
                p1 += num
            
        return p1 == len(word) and p2 == len(abbr)


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Two Pointers, j for abbr, i for word
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            # If it's a letter, check if they are the same because letters must match
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                # If it's a number, get the full number
                # no leading zero
                if abbr[j] == '0':
                    return False
                num = 0
                # get the full number
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                # Move the pointer in word by that number since that number means we skip that many characters
                i += num
        
        # if we reach the end of both word and abbr, then it's a valid abbreviation.
        return i == len(word) and j == len(abbr)
