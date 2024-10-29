class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0
        char_dict = {}
        for right in range(len(s)):
            if s[right] in char_dict:
                char_dict[s[right]] += 1
            else:
                char_dict[s[right]] = 1
            
            # find the the letters in the window with most frequencies
            max_freq = max(max_freq, char_dict[s[right]])
            # plus 1 because of the zero index, without the max frequency number, we only allow 
            # k number of other replacements and we keep moving left until we satisfy the condition
            while right - left + 1 - max_freq > k:
                char_dict[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
