# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # my own answer for this question, but probably not optimal
        # create a window that is size of 10 and move it to the end to see if there is any duplicates through the move
        sequence_set = set()
        return_list = set()

        if len(s) < 10:
            return []

        print(len(s))
        for right in range(10, len(s) + 1):
            left = right - 10
            if s[left:right] in sequence_set:
                return_list.add(s[left:right])
            else:
                sequence_set.add(s[left:right])        

        return list(return_list)