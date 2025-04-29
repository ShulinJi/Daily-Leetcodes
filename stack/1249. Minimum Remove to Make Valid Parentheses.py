# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(n) space and time complexity
        # set of indexes to remove after traverse 
        index_to_remove = set()
        # stack to store indexes of "(" where we need a pending ")"
        stack = []
        for i, char in enumerate(s):
            # if it is not parenthese, continue
            if char not in "()":
                continue
            # if it is (, then we add it to the stack wating for its pair )
            if char == "(":
                stack.append(i)
            # if stack is empty and we find a ), then need to remove this b/c it won't be paired
            elif not stack:
                index_to_remove.add(i)
            # else, we find ) and have a pending (, we pop that (.
            else:
                stack.pop()
        
        # add whatever left in stack to removal list b/c it is unpaired
        while stack:
            index_to_remove.add(stack.pop())

        answer = ""
        for i in range(len(s)):
            if i not in index_to_remove:
                answer += s[i]
        return answer
