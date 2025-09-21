# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

# O(n) time | O(n) space
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        current_number = 0
        # we add a '+' operator at the beginning to handle the first number
        curr_operator = '+' 
        for i in range(len(s)):
            curr_char = s[i]
            # if the current character is a digit, we build the current number ex. 32 -> 3*10 + 2 = 32
            if s[i].isdigit():
                current_number = current_number * 10 + int(curr_char)
            # if the current character is an operator or we are at the end of the string, we evaluate the expression, we skip spaces
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if curr_operator == '-':
                    stack.append((-1) * current_number)
                elif curr_operator == '+':
                    stack.append(current_number)
                elif curr_operator == '*':
                    # we pop the last number from the stack and multiply it with the current number
                    prev = stack.pop()
                    stack.append(prev * current_number)
                elif curr_operator == '/':
                    # we pop the last number from the stack and divide it with the current number
                    # we use int() to truncate towards zero, // (floor) won't work for negative numbers
                    prev = stack.pop()
                    stack.append(int(prev / current_number))

                # update the current operator and reset the current number after evaluation
                curr_operator = curr_char
                current_number = 0
        
        # we sum up all the numbers in the stack to get the final result, we only have + and - operators in the stack
        while stack:
            result += stack.pop()
        
        return result