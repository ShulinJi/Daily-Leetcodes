# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

# Note that operands in the returned expressions should not contain leading zeros.

 

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
# Example 3:

# Input: num = "3456237490", target = 9191
# Output: []
# Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

# Constraints:

# 1 <= num.length <= 10
# num consists of only digits.
# -231 <= target <= 231 - 1

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        answers = []
        def backtrack(index, pre_operand, current_operand, value, string):
            if index == N:
                # to check current_operand == 0, it means we have already done the operation and there is no in-progress digits
                # if not == 0, it means we still have digits that are waiting for itself to get assigned an operator, but we already reached the end, so not valid
                # we need to assign operator earlier than this, b/c there is no num[N]
                if value == target and current_operand == 0:
                    # string[1:] because we ignore the very first sign at the beginning of operation
                    answers.append("".join(string[1:]))
                return 
            
            # if we did + or - or *, the current_operand would be 0, and current_operand would just be the normal num[index]
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)

            # we try to combine digits together, current_operand will be passed down to form new digits
            # Use current_operand > 0 to avoid combine digits like "05"
            if current_operand > 0:
                backtrack(index + 1, pre_operand, current_operand, value, string)
            
            # we try addition
            string.append("+")
            string.append(str_op)
            backtrack(index + 1, current_operand, 0, value + current_operand, string)
            string.pop()
            string.pop()

            # if we are at the start of the operation
            if string:
                # we try subtraction
                string.append("-")
                string.append(str_op)
                backtrack(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop()
                string.pop()

                # we try multiplication
                string.append("*")
                string.append(str_op)
                # we first undo the previous operand by value - pre_operand, and then we perform multiplication to ensure logical correctness (first * then + or -)
                backtrack(index + 1, current_operand * pre_operand, 0, value - pre_operand 
                + (current_operand * pre_operand), string)
                string.pop()
                string.pop()

        backtrack(0, 0, 0, 0, [])
        return answers