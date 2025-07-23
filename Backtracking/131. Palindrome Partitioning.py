# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, [], result)
        return result

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def dfs(self, s: str, path: List[str], result: List[List[str]]):
        # Base case which we have exhausted all the remaining string, means all the components are palindrome
        if not s:
            result.append(path)
            return
        
        for i in range(1, len(s) + 1):
            # we don't add a break if it's not palindrome because we want to check longer substrings. ex. ab is not, but aba is
            if self.isPalindrome(s[:i]):
                # add current substring in the currentList, s[i:] is the rest of the string, don't need to remove element from path since it is just a copy
                self.dfs(s[i:], path + [s[:i]], result)
                # backtrack and remove the current substring from currentList