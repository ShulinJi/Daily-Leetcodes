# 383. Ransom Note
# Solved
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if len of ransomNote is larger than magazine, then it is not possible to contruct
        if len(ransomNote) > len(magazine):
            return False
        
        # Use a hashmap to record the number of appearance of each letter in ransomNote
        hashmap = {}
        for x in magazine:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        
        # Decrease the number of appearance of each character whenever we use it, and return false if it runs out of the characters
        for x in ransomNote:
            if x in hashmap:
                if hashmap[x] == 0:
                    return False
                else:
                    hashmap[x] -= 1
            else:
                return False
        return True
        