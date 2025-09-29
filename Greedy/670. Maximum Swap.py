# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 

# Constraints:

# 0 <= num <= 108

# brute force
# O(n^2) time | O(n) space
class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = num
        num_list = list(str(num))

        for num1 in range(len(num_list)):
            for num2 in range(num1, len(num_list)):
                new_num = num_list[:]
                new_num[num1], new_num[num2] = new_num[num2], new_num[num1]
                curr_num = int(str(''.join(new_num)))
                max_num = max(max_num, curr_num)
        
        return max_num