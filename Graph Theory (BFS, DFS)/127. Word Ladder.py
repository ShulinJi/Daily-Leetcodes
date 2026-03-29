# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        visited = set()
        visited.add(beginWord)

        queue = deque([beginWord])
        # we start at 1 b/c the transformation sequence count the first one
        turn = 1

        # BFS
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return turn
                for word in word_set:
                    # if the length does not equal, we skip this choice
                    if len(word) != len(curr_word):
                        continue
                    
                    # traverse through all the words and find the ones that are only one letter difference
                    word_diff = 0
                    for i in range(len(word)):
                        if word[i] != curr_word[i]:
                            word_diff += 1
                            if word_diff > 1:
                                break
                    if word_diff == 1 and word not in visited:
                        queue.append(word)
                        visited.add(word)
            
            turn += 1

        return 0