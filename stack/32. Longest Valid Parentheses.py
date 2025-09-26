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