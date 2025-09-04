# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        # use a * 10 because for 3 and 30, 
        # lexicographically 3 < 30 < 34, but the actual order should be 34 3 30 to maximize
        # so we repeat the string 10 times and 3 -> "333333..", 30 -> "3030303...", "34" -> "34343434.."
        # this way when we compare the string, 34 > 3 > 30
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)