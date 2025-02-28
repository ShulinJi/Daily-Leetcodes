class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            # if we use the defualt dict, then we need to check the 
            anagram_s = tuple(sorted(s))
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