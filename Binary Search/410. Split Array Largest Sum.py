# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= k <= min(50, nums.length)

# SECOND ATTEMPT
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def calculateSplitNumbers(maxSum):
            totalSplit = 0
            currSum = 0
            for num in nums:
                if currSum + num > maxSum:
                    currSum = num
                    totalSplit += 1
                else:
                    currSum += num
            return totalSplit + 1
        
        left = max(nums)
        right = sum(nums)
        bestSum = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            print(left, right)
            # calculateSplitNumbers is the function that calculate the minimum number of subarray given current maxSum
            # but sometimes we have bestSum but with fewer than allowed cut (k), which is also the optimal
            # ex, [2,3,1,1,1,1,1], allowde is 5, but we can only make bestSum to 3 since max(arr) = 3 and calculateSplitNumbers return 4 instead of 5, so we should use <=, instead of == to check calculateSplitNumbers(mid) since if calculateSplitNumbers(mid) gives us a answer <= k, it means it is a valid maxSum! if it's smaller, we can just add more cuts randomly.
            if calculateSplitNumbers(mid) <= k:
                # we should keep trying if we find a valid answer to find minimum
                # try to make the sum smaller and see if it changes
                bestSum = min(mid, bestSum)
                right =  mid - 1
            else:
                # we need more than allowed k subarrays
                left = mid + 1
        
        return bestSum


# O(n log m) time complexity where n is the number of elements in nums and m is the range of possible sums (from max(nums) to sum(nums)).
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we first set a number X that is greater than or equal to the maximum element in nums so that no single element exceeds X 
        # and we can split the array accordingly. Then this function calculates the minimum number of subarrays needed such that 
        # no subarray has a sum greater than X by iterating through the array and accumulating the sum of elements until adding another element would exceed X.
        # which means we need to start a new subarray and increment the count of subarrays.(split + 1)
        # then if the calculated number of subarrays is less than or equal to k, we try to find a smaller maximum sum by adjusting the right boundary.
        # otherwise, we need to increase the maximum sum by adjusting the left boundary.

        def min_subarray_required(max_sum):
            current_sum = 0
            splits_required = 0

            for element in nums:
                if current_sum + element <= max_sum:
                    current_sum += element
                else:
                    current_sum = element
                    splits_required += 1
            
            return splits_required + 1
        
        # left is the minimum possible largest sum (the largest single element in nums) because we cannot have a subarray with a sum less than the largest element.
        # right is the maximum possible largest sum (the sum of all elements in nums) because one valid split is to have all elements in one subarray.
        left = max(nums)
        right = sum(nums)
        minimum_largest_split_sum = None

        # won't have infinite loop because left and right will converge because right and left are both updated after each iteration
        while left <= right:
            max_allowed = (left + right) // 2
            if min_subarray_required(max_allowed) <= k:
                right = max_allowed - 1
                minimum_largest_split_sum = max_allowed
            else:
                left = max_allowed + 1
        
        return minimum_largest_split_sum
        
