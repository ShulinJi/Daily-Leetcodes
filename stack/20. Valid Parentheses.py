class Solution:
    def isValid(self, s: str) -> bool:
        # Add a check when the length of the string cannot module by 2 -> false directly
        if len(s) % 2:
            return False


        stack = []
        # we map the 
        mapping = {'}':'{', ']': '[', ')': '('}

        for char in s:
            if char in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    return False
                
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack








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
            
