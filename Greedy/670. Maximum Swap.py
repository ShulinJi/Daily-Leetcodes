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

# O(n) time | O(n) space
# Greedy
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        max_right_index = [0] * n
        max_right_index[n - 1] = n - 1

        # One pass to fill the max_right_index array
        for i in range(n - 2, -1, -1):
            max_right_index[i] = i if num_list[i] > num_list[max_right_index[i + 1]] else max_right_index[i + 1]
        
        # if we find a digit that is less than the max digit on its right, we swap and return the result
        # because earliest such swap will yield the maximum result
        for i in range(n):
            if num_list[i] < num_list[max_right_index[i]]:
                num_list[i], num_list[max_right_index[i]] = num_list[max_right_index[i]], num_list[i]
                return int("".join(num_list))
        
        return num

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