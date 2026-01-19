# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# SECOND ATTEMPT
class Solution:
    def subsets(self, nums):
        # O(N * 2^N) becaseu 2^n to generate all possible subset, and O(n) to copy the path
        def backtracking(start, path):
            # whenever we have a path, it is valid
            ans.append(path[:])

            # to avoid the duplicate, we never traverse backwards and start with i + 1
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        ans = []
        backtracking(0, [])
        return ans 


class Solution:
    def subsets(self, nums):
        self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        # Add the current subset to the output
        self.output.append(curr[:])
        # Generate subsets starting from the current index
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()
