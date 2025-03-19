# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # O(n) runtime, O(n) space
        # return list for the result
        return_interval = []

        # we start the loop at the beginning
        i = 0
        while i < len(nums):
            # it is a new start of an interval
            start = nums[i]
            # we keep traversing until we find a discontinued number, ex: 1, 2, 3, 6, we stop at 3stack
            
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            # then we check if our start has ever been changed or not, it yes, then we have a interval "1 -> 3"
            if start != nums[i]:
                return_interval.append(str(start) + "->" + str(nums[i]))
            # if the start is not changed, then it is the number itself, no interval, "6"
            else:
                return_interval.append(str(start))
            # we increment because we include the end of interval already and need to move forward to next number
            i += 1
            
        return return_interval