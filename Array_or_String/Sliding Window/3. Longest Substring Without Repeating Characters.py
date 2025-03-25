class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # uniqueString = set()
        # longest = 0
        # start = 0

        # x = 0
        # while x < len(s):
        #     if s[x] in uniqueString:
        #         if len(uniqueString) > longest:
        #             longest = len(uniqueString)
        #         uniqueString.clear()
        #         start += 1
        #         if start < len(s):
        #             x = start
        #             continue
        #         else:
        #             break
        #     else:
        #         uniqueString.add(s[x])

        #     if x == len(s) - 1:
        #         if len(uniqueString) > longest:
        #             longest = len(uniqueString)
        #     x += 1

      # Faster with dictionary search
      # Move the left to the index where we just passed the one that caused duplication
      # char_index[char] >= left so that previous elements won't interfer with current window
      # Ex. [a, b, c, d, b, e, f, g, a] we have 2 b in the array which would cause our left to shift to 2, when we encounter 'a' again at 8
      # we haven't updated index of a, which is still 0, if we don't check index >= left, then it would be counted as duplicate as well, but in fact. 
      # the a before left does not have an impact because if there's already a duplicate happened before (we moved left, there's duplicate b) the array that contains 2b are also not valid!
        # it is to ensure that the char we are checking are inside the sliding window! if index is smaller than left bound, then we don't need to check!
    
        char_index = {}
        left = 0
        right = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in char_index:
                # + 1 b/c we want to update our left one over the duplicate, so +1 makes it to next element
                # b/c if we don't plus one, for example, "dabca" we jump to the index 1 which is first a but it still include the a, which is still duplicate
                left = max(left, char_index[s[right]] + 1)

            # record the index of this element
            char_index[s[right]] = right
            ans = max(ans, right - left + 1)
        
        return ans




        # Same method here! 

        char_index = {}
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
