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