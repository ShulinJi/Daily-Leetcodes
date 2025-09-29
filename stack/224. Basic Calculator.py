# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

class Solution:
    def evaluate(self, stack):
        res = 0
        # if the stack is empty or the top element is an operator, we push 0 to handle cases like "-2+1" or "(-2+1)"
        # so that we can pop 0 and apply the operator correctly
        if not stack or type(stack[-1]) == str:
            stack.append(0)
        # first element will always be a number
        res = stack.pop()
        while stack and stack[-1] != ")":
            # next element will always be an operator
            sign = stack.pop()
            # pop the number and apply the operator
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        # we traverse the string in reverse order so that we can easily handle - as a unary operator
        # because we are pushing to stack, if we don't reverse, the order poped from stack for - will be in correct order
        # example: "1 - 2 + 3", if we traverse from left to right, stack will be [1, '-', 2, '+', 3], when we pop, we will get 3 first, then +, then 2, then -, then 1
        # which will be evaluated as 3 + 2 - 1 = 4, which is incorrect
        for i in range(len(s) - 1, -1, -1):
            # if the character is a digit, we keep building the operand in reverse order
            if s[i].isdigit():
                operand = (10 ** n * int(s[i])) + operand
                n += 1
            elif s[i] != " ":
                # if n is not 0, we have an operand waiting to push to stack and reset n and operand for next operand
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                #  if the character is an opening bracket "(", we evaluate the expression till we find the closing bracket
                # else we just push the operator or closing bracket to stack "+ - )"
                if s[i] == "(":
                    res = self.evaluate(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(s[i])
        if n:
            stack.append(operand)
        
        return self.evaluate(stack)