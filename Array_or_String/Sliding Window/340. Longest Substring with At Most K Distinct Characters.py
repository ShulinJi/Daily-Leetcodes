# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 0 <= k <= 50

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        word_dict = {}
        left = 0
        max_length = 0

        for i in range(len(s)):
            if s[i] not in word_dict:
                word_dict[s[i]] = 1
            else:
                word_dict[s[i]] += 1

            # if len of the dict is greater than the target, it means that there are more than k distinct characters
            # we need to pop it to get valid sub array
            while len(word_dict) > k:
                word_dict[s[left]] -= 1
                if word_dict[s[left]] == 0:
                    del word_dict[s[left]]
                left += 1
            max_length = max(max_length, i - left + 1)
        
        return max_length


# second attemtpt
# O(n) time and O(k) space
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        currentWindow = dict()
        ans = 0

        for right in range(len(s)):
            if s[right] in currentWindow:
                currentWindow[s[right]] += 1
            else:
                currentWindow[s[right]] = 1
            
            while len(currentWindow) > k:
                currentWindow[s[left]] -= 1
                if currentWindow[s[left]] == 0:
                    del currentWindow[s[left]]
                left += 1
            ans = max(ans, right - left + 1)

        return ans