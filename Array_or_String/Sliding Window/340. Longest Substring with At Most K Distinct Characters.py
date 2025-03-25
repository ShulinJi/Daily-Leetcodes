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