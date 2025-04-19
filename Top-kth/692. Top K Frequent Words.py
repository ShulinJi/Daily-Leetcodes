# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

# Constraints:

# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
 

# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        # compare freq first, then if equal then we compare order of words
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        result = []
        for word, freq in word_freq.items():
            heapq.heappush(result, Pair(word, freq))
            if len(result) > k:
                heapq.heappop(result)
            # if len(result) < k:
            #     heapq.heappush(result, Pair(freq, word))
            # else:
            #     if freq > result[0].freq:
            #         heapq.heappop(result)
            #         heapq.heappush(result, Pair(freq, word))

        res = [0] * len(result)
        index = len(result) - 1
        while result:
            word = heapq.heappop(result).word
            res[index] = word
            index -= 1
        return res

