class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pair_dict = {'(': ')', '{': '}', '[':']'}

        # Stack: first in, last out, can use list pop() and append()
        stack = []
        for x in range(len(s)):
            # Append all the left side of parenthese
            if s[x] == '{' or s[x] == '[' or s[x] == '(':
                stack.append(s[x])
            else:
                if len(stack) == 0:
                    return False
                # Whenever we met a right parenthese, we check its corresponding left side
                # which is the last element in list (first element in queue) by pop
                # if the left side doesn't match, then False
                last_parenthese = stack.pop()
                if pair_dict[last_parenthese] != s[x]:
                    return False

        # if there are any unmatched parenthese after going through whole string
        if len(stack) > 0:
            return False

        return True
            
