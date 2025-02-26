class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stringList = ''.join([x.lower() for x in s if x.isalpha() or x.isdigit()])
        # j = len(stringList) - 1
        # for i in range (len(stringList) // 2):
        #     if stringList[i] != stringList[j]:
        #         return False
        #     j = j - 1
        # return True
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
                continue

            while not s[r].isalnum() and l < r:
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                r -= 1
                l += 1

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
