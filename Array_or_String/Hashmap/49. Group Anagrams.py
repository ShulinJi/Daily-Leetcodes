# 49. Group Anagrams
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


# O(N*K) runtime, O(N*K) space complexity
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            # reset the count for each string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # use tuple to make it hashable, use count as the key to group anagrams together since they have the same character count for anagrams
            ans[tuple(count)].append(s)
        return list(ans.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(NKlogK) runtime, O(NK) space complexity
        # use collection.defaultdict, which it initialize the entries automatically, 
        # don't need to check if a key exists or not
        ans = collections.defaultdict(list)
        for s in strs:
            # Convert to tuple to make it hashable
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())




        answer = {}
        for s in strs:
            # if we use the defualt dict, then we need to check if the key exist or not
            # A list is not hashable, need to use something not immutable, such as, string, tuple, integers...
            # List can be modified in-place, so the hash value may get changed
            anagram_s = tuple(sorted(s))
            # if not exist, we need to first initialize it, cannot directly append
            if anagram_s not in answer:
                answer[anagram_s] = []
                answer[anagram_s].append(s)
            else:
                answer[anagram_s].append(s)
        
        return list(answer.values())




        # works
        # dictionary used to record group of index with the same anagram
        anagram_groups = {}
        for x in range(len(strs)):
            current_word = ''.join(sorted(strs[x]))
            if current_word in anagram_groups:
                anagram_groups[current_word].append(x)
            else:
                anagram_groups[current_word] = [x]

        # access the index and group it 
        res = []
        for x in anagram_groups:
            current_group = []
            for y in anagram_groups[x]:
                current_group.append(strs[y])
            res.append(current_group)

        return res



        # Exceed Time Limit, but it works
        # res = []
        # current_group = []
        # for x in range(len(strs)):
        #     if strs[x] == True:
        #         continue
        #     current_word = sorted(strs[x])
        #     current_group = [strs[x]]
        #     for y in range(x+1, len(strs)):
        #         if strs[y] == True:
        #             continue
        #         if sorted(strs[y]) == current_word:
        #             current_group.append(strs[y])
        #             strs[y] = True
        #     res.append(current_group)
        # return res