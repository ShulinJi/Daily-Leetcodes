# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

#  stack solution
# O(n) time | O(n) space
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        if not s:
            return 0
        # stack[-1] is the index of the last unmatched ')'
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                # if stack is empty, it means we have matched all the previous '(', so we push the index of the current ')'
                # this index will be used to calculate the length of the valid substring when we find a matching ')'
                # complex example: "())(())", when we are at the second ')', we pop the index of the first '(', and the stack becomes empty
                # we push the index of the second ')', which is 2, at the i = 6 and the stack is [2], so the length of the valid substring is 6 - 2 = 4
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
        
# O(n) time | O(1) space
# No stack, no DP, two pass solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        # left to right, count number of left and right parentheses

        # Basic idea: whenever we have left == right, we have a valid substring because we avoided cases like ))(, ()) that right > left from left to right
        # which makes it invalid and we reset the count to 0 to start over, and from right to left, we use left > right to avoid cases like ((), ())(
        # that left > right from right to left which makes it invalid, and we reset the count to 0 to start over
        # since left == right, 2*right or 2*left is the length of the valid substring, and we just keep track of the max length

        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0
        
        return max_length

# O(n) time | O(n) space
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            # we only care about the closing parenthesis, because a valid parentheses must end with a closing parenthesis
            if s[i] == ')':
                # case 1: if the previous character is '(', then we have a valid pair, we add 2 to the result of the substring ending two characters before
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                # case 2: if the previous character is ')', we check if the character before the valid substring ending at i-1 is '(', if it is, then we have a valid pair
                # example: "(()())", when we are at the last ')', we check if the character before the valid substring "()" is '(', if it is, then we have a valid pair
                # we add 2 to the result of the substring ending at i-1, and also add the result of the substring ending before the matching '(' that extends the valid substring
                elif s[i - 1] == ')' and i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    if i >= 2:
                        # -2 because we are checking the character before the matching '(', try to entend before "(()())"
                        # +2 is the current valid pair
                        # dp[i - 1] is the length of the valid substring ending at i-1, refer to example as the second last ) in "(()())", should be 4
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2

                max_length = max(max_length, dp[i])
        return max_length


