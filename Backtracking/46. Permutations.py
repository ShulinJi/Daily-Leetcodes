# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # need to keep track what we have so far to record ans and check ans
        def backtracking(path):
            if len(path) == len(nums):
                ans.append(path[:])
            
            # since the numbers are distinct, as long as we a number that is not in the path, we add it, which is valid!
            # and we just start at different index and form different permutations
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(path)
                    path.pop()


        ans = []
        backtracking([])
        return ans
     

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time complexity, what you should say in an interview: O(n⋅n!)
        ans = []
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(list(curr))
                return 
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                
        backtrack([])
        return ans
