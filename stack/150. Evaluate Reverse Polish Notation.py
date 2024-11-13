class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # used to store the numbers
        for i in range(len(tokens)):
            # if current token is a number, not an operator, we simply store it fr later use
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                # if current token is an operator, we check which operator it is
                # and do the operation for the previous two numbers 
                # after the operation we append the result back to the stack
                num2 = stack.pop()
                num1 = stack.pop()

                result = 0
                if tokens[i] == '+':
                    result = num1 + num2
                elif tokens[i] == '-':
                    result = num1 - num2
                elif tokens[i] == '*':
                    result = num1 * num2
                elif tokens[i] == '/':
                    result = int(num1 / num2)

                stack.append(result)
        
        return stack[-1]

        # Brute force, whenever we find a operator, we calculate the previous two numbers
        # O(n^2) speed and O(1) space
        # current_position = 0

        # while len(tokens) > 1:

        #     # Move the current position pointer to the next operator.
        #     while tokens[current_position] not in "+-*/":
        #         current_position += 1

        #     # Extract the operator and numbers from the list.
        #     operator = tokens[current_position]
        #     number_1 = int(tokens[current_position - 2])
        #     number_2 = int(tokens[current_position - 1])

        #     # Calculate the result to overwrite the operator with.
        #     if operator == "+":
        #         tokens[current_position] = number_1 + number_2
        #     elif operator == "-":
        #         tokens[current_position] = number_1 - number_2
        #     elif operator == "*":
        #         tokens[current_position] = number_1 * number_2
        #     else:
        #         tokens[current_position] = int(number_1 / number_2)

        #     # Remove the numbers and move the pointer to the position
        #     # after the new number we just added.
        #     tokens.pop(current_position - 2)
        #     tokens.pop(current_position - 2)
        #     current_position -= 1

        # return int(tokens[0])


# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

