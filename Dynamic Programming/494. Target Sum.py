# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

# O(n * sum(nums)) time complexity, O(n * sum(nums)) space complexity
# backtracking with memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        # We need to offset the sum by total_sum so that we can use negative indices (from -1000 to 1000)
        memo = [[float('-inf')] * (2 * total_sum + 1) for _ in range(len(nums))]

        def calculate_ways(current_index, current_sum):
            # Base case: if we have reached the end of the array, check if the current sum equals the target
            if current_index == len(nums):
                return 1 if current_sum == target else 0
            else:
                # use + total_sum to offset negative indices to cover the range from -1000 to 1000
                # if we have already calculated the number of ways for this state, return it

                # Where "identical branches" appear
                # Notice that (index=2, sum=-1) appears in two different ways:
                # From (index=1, sum=1) → subtract 2
                # From (index=1, sum=-1) → add 0
                # Even though the paths are different, the subproblem is the same:
                # "At index 2, with a current sum of -1, how many ways can I reach the target?"
                if memo[current_index][current_sum + total_sum] != float('-inf'):
                    return memo[current_index][current_sum + total_sum]

                # Calculate the number of ways to reach the target by either adding or subtracting the current number
                add = calculate_ways(current_index + 1, current_sum + nums[current_index])
                minus = calculate_ways(current_index + 1, current_sum - nums[current_index])

                # Store the result in the memoization table
                memo[current_index][current_sum + total_sum] = add + minus
            
            return memo[current_index][current_sum + total_sum]
        
        return calculate_ways(0, 0)