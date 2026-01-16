# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

# SECOND ATTEMPT
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(curr_sum, path, start):
            if curr_sum == target:
                ans.append(path[:])
            elif curr_sum > target:
                return 
            
            # because we have distinct integers and we are either staying or moving forward
            # it won't have duplicate cases! ex: target 7, candidates = [2,3,6,7], we could only have [2, 2, 3]
            # but there is no way to have [2, 3, 2] because we are not able to go backward

            # we use start, not start +1 to allow use of same number unlimited number of times.
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                curr_sum += candidates[i]
                
                backtracking(curr_sum, path, i)
                curr_sum -= candidates[i]
                path.pop()
        
        backtracking(0, [], 0)
        return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return list
        results = []
        def backtrack(remaining, combination, start):
            # if the remaining is 0, then we find the combination
            if remaining == 0:
                results.append(list(combination))
            # if the remaining is < 0, then this combination is not valid, directly return
            elif remaining < 0:
                return 
            
            # then we try all the possible combination with all candidates
            for i in range(start, len(candidates)):
                # form new combination with new candidates
                combination.append(candidates[i])
                # start new backtracking
                backtrack(remaining - candidates[i], combination, i)
                # we remove the combination since we have checked all the possible branches on this candidates
                combination.pop()

        backtrack(target, [], 0)
        return results
