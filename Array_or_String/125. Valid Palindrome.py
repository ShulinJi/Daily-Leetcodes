class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stringList = ''.join([x.lower() for x in s if x.isalpha() or x.isdigit()])
        # j = len(stringList) - 1
        # for i in range (len(stringList) // 2):
        #     if stringList[i] != stringList[j]:
        #         return False
        #     j = j - 1
        # return True
        
        
        i, j = 0, len(s) - 1
        while i < j:
            # Move i to the next alphanumeric character or stop if past j
            while i < j and not s[i].isalnum():
                i += 1
            # Move j to the previous alphanumeric character or stop if before i
            while i < j and not s[j].isalnum():
                j -= 1
            # Compare characters, converting them to lowercase
            if s[i].lower() != s[j].lower():
                return False
            # Move pointers inward
            i += 1
            j -= 1
        return True




# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
