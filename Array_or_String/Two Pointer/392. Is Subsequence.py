# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

# SECOND ATTEMPT, O(n), O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        return p1 == len(s)




# Solution for the FOLLOW UP
# Since t is fixed and reused, I preprocess the indices of each character and binary search those index lists to find increasing positions efficiently
from bisect import bisect_right
from collections import defaultdict

class Solution:
    # we first process the t since there are a lot of s, so this we only need to process t once
    # O(n), O(n)
    def __init__(self, t: str):
        self.pos = defaultdict(list)
        # dictionary for key is the character and vale is a list of index which it appears
        for i, ch in enumerate(t):
            self.pos[ch].append(i)

    def isSubsequence(self, s: str, t: str) -> bool:
        # the current index of t, we keep track of this to avoid 
        curr = -1
        for ch in s:
            # if the character not in the dictionary, return false
            if ch not in self.pos:
                return False
            
            # initially curr is -1, then it will be 0, the first one of the list
            # binary search to find the index that the curr could be inserted after curr, so that all elements before
            # curr is <= curr
            idx = bisect_right(self.pos[ch], curr)
            # if the current index is bigger than every element in the list, binary search will return the last index
            # which means we could only insert at the last index, then it means there is no available characters for  
            # current situation, so return false
            if idx == len(self.pos[ch]):
                return False
            
            # update the current index of t to make sure it is strictly increating
            curr = self.pos[ch][idx]
        
        return True



# Two Pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # get the bound for s and t (the bound which the pointer would stop at)
        leftBound = len(s)
        rightBound = len(t)

        # we will slide our pointer whenever we find there is a match for left and right
        # This ensures the order since we slide from left to right
        left = 0
        right = 0
        while left < leftBound and right < rightBound:
            if s[left] == t[right]:
                left += 1
            right += 1

        # then we only need to check if the pointer has travelled through all s, meaning that all characters in s have been found in t
        # which implies that s is a subsequence of t
        return left == leftBound 

