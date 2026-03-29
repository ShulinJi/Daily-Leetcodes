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



# Optimized approach, using bi-directional BFS, we can start from both end and start word, and meet in the middle, 
# this way we can reduce the search space by half, and we can also use a dictionary to store the intermediate words that are one letter different, 
# so we can quickly find the next words to explore instead of traversing through the whole word list every time, 
# this way we can reduce the time complexity from O(n^2) to O(n * m) where n is the number of words in the word list and m is the length of the words. 
# The space complexity is O(n * m) for storing the intermediate words in the dictionary.

from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.length: int = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict: Dict[str, List[str]] = defaultdict(list)

    def visitWordNode(
        self,
        queue: Deque[str],
        visited: Dict[str, int],
        others_visited: Dict[str, int],
    ) -> Any:
        queue_size: int = len(queue)
        for _ in range(queue_size):
            current_word: str = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word: str = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )

                # Next states are all the words which share the same intermediate state.
                for word in self.all_combo_dict[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queues for birdirectional BFS
        queue_begin: Deque[str] = collections.deque(
            [beginWord]
        )  # BFS starting from beginWord
        queue_end: Deque[str] = collections.deque(
            [endWord]
        )  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin: Dict[str, int] = {beginWord: 1}
        visited_end: Dict[str, int] = {endWord: 1}
        ans: Any = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(
                    queue_begin, visited_begin, visited_end
                )
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

# This approach is very slow, not optimized
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