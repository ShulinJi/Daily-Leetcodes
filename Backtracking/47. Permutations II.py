# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# SECOND ATTEMPT
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # time complexity is the same of the number of nodes in a tree, 
        # If the counts of repeated numbers are: c1, c2, ..., cm   (sum = N). number of unique permutations is: N! / (c1! · c2! · ... · cm!), which is the Level k → P(N, k)
        # then we sum up all the levels :O(N · (N! / (c1! · c2! · ... · cm!))), upper bound would be O(n!n) and O(n)
        def backtracking(path, counter):
            if len(path) == len(nums):
                ans.append(path[:])
            
            # we convert the list to a hashmap, in thi way, we can know how many duplicates we can have 
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtracking(path, counter)
                    counter[num] += 1
                    path.pop()
        

        ans = []
        # similar to Permutation I, but this time we are using a counter map to check if the number is visited already
        # this time we have duplicate, we cannot use the if in simple mechnism to check 
        backtracking([], Counter(nums))
        return ans


# O(n * n!) time | O(n) space
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtracking(comb, counter):
            # if the combination is the same length as the input, we found a permutation
            if len(comb) == len(nums):
                results.append(list(comb))
            
            for num in counter:
                # if the count of the number is more than 0, we can use it
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtracking(comb, counter)
                    comb.pop()
                    counter[num] += 1
        
        # since we want to avoid duplicates, we can use a counter to keep track of the count of each number
        #  use a counter so that we treat duplicates as one number. ex [1,1,2] -> {1:2, 2:1} then we avoid the cases like
        #  we pick 1 at index 0 to get 1, 1, 2 and then start at index 1 to get 1, 1, 2 again, which treats two 1 as different numbers
        backtracking([], Counter(nums))
        return results
