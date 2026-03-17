# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # O(n * k), n is the len of words array, and k is the length of each string
        if not words:
            return []
        
        # pick the shortest string because if a letter occurs in all string, it needs to be every string
        global_letter_counter = Counter(min(words, key=len))

        # we iterate each word and we take the min of each occurance, then after iteration, we have the common ones with 1 or greater! in this way, we record the occurance and count
        for i in range(1, len(words)):
            current_word_counter = Counter(words[i])
            for letter in global_letter_counter:
                global_letter_counter[letter] = min(
                    current_word_counter[letter], 
                    global_letter_counter[letter]
                )

        # then we just need to print out based on the count
        ans = []
        for letter, count in global_letter_counter.items():
            if count == 0:
                continue
            else:
                for _ in range(count):
                    ans.append(letter)
        
        return ans
                    
