# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


# bottom-up approach 
# [False, False, False, False, True, False, False, True, False, False, False, False, True]
# this is the output for example "applepenapple", and ["apple","pen"]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        
        for i in range(len(s)):
            # check for each word that if it can form a word in the wordDict
            for word in wordDict:
                # only serve for the purpose of first word (initial condi) that could happen that i < len(word)
                if i < len(word) - 1:
                    continue
                
                # check dp[i - len(word)] so that this is a valid start (we can continue form words from there)
                # i == len(word) - 1 only for the first word purposes! 
                if dp[i - len(word)] or i == len(word) - 1:
                    # we check if the words are matching 
                    if s[i - len(word) + 1: i + 1] == word:
                        # if yes, we found a word that matches and break
                        dp[i] = True
                        break
                    
        # if the last one is True, meaning that we have went through all the string and found out that every words have a match 
        return dp[-1]


# top-down approach, mem-recursion approach
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top-down approach
        @cache
        def dp(i):
            # if we reach the 0 and call dp(-1), means all the previous search has been met, which implies that all previous search are true
            # so the whole search tree is true b/c we need and dp(i - len(word)) condition to be met b/c if cannot reach 0 if it returned false
            # it means the string is breakable!
            if i < 0:
                return True

            for word in wordDict:
                # for each word, check if the word matches and if its previous string are also breakable (both have to meet to ensure that our words 
                # start at the correct index (not jumping through indexes))
                if s[i - len(word) + 1: i + 1] == word and dp(i - len(word)):
                    return True
            
            return False
    
        return dp(len(s) - 1)