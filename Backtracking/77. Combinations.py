# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

# SECOND ATTEMPT
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start, path):
            if len(path) == k:
                ans.append(path[:])
                return

            # find in the range of [start, n]
            # to avoid duplicate, we only choose from left to right by counting a start point, 
            # so that in next branch we never go back to previous values
            for i in range(start, n + 1):
                path.append(i)
                # use i + 1 because we only allow to use it once
                backtracking(i + 1, path)
                path.pop()

        ans = []
        backtracking(1, [])
        return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, first_num):
            # if we have found k element already, we copy the list by either list(), or curr[:], otherwise, we only copied the address
            if len(curr) == k:
                ans.append(list(curr))
                return 
            
            # we try to find all possible solutions and avoid duplicate by only considering the ones that's bigger than current number
            for num in range(first_num, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
        
        backtrack([], 1)
        return ans


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, first_num):
            if len(curr) == k:
                ans.append(list(curr))
                return 
            
            # extra method to prune the ones that already gurantee to fail!
            # ex. n = 5, k = 3, then we are at curr = [4], and there is no way we could get an valid answer through this pass, so we don't explore [4, 5]
            needed = k - len(curr)
            remain = n - first_num + 1
            available = remain - needed
            for num in range(first_num, first_num + available + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
        
        backtrack([], 1)
        return ans
