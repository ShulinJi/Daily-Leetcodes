# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# SECOND ATTEMPT
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2^n) and O(n)
        def backtracking(curr_sum, path, start):
            if curr_sum == target:
                ans.add(tuple(path[:]))
            # some early prune since all candidates are positive
            elif curr_sum > target:
                return

            for i in range(start, len(candidates)):
                # we prune the duplicate branches early, avoid cases like [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                # and we use i > start so that we ensure that the start is actually being touched instead of prunning 
                # every possible one, we still capture the case where all ones are used to achieve the atrget
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr_sum += candidates[i]
                path.append(candidates[i])
                backtracking(curr_sum, path, i + 1)
                curr_sum -= candidates[i]
                path.pop()
        
        candidates.sort()
        ans = set()
        backtracking(0, [], 0)
        return [list(x) for x in ans]



# time limit exceeded on large test cases like 100 candidates with value 1 and target 30
# O(2^n) time complexity in the worst case, where n is the number of candidates. This is because, in the worst case, we may explore all possible combinations of candidates.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort candidates to handle duplicates and make it easier to manage combinations
        candidates.sort()
        results = set()
        def backtracking(remain, comb, start):
            if remain == 0:
                results.add(tuple(comb))
            elif remain < 0:
                return 
            
            for i in range(start, len(candidates)):
                # so, since we want to avoid duplicates, it doesn't matter which 1 we pick, we only need 1 because all others are the same (result duplicate), 
                # but we don't ignore the first one (default one), then we cna cover all the cases and we only need 101 branches
                # prunes the tree by skipping over duplicate candidates at the same recursive depth
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtracking(remain - candidates[i], comb, i + 1)
                comb.pop()
            
        backtracking(target, [], 0)
        return [list(x) for x in results]
