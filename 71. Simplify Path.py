class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split("/"):
            # if there's a .., means we go back to our last directory, we pop the last element in stack
            if portion == '..':
                if stack:
                    stack.pop()
            # we have . or empty directory, means current directory, do nothing
            elif not portion or portion == '.':
                continue
            else:
                stack.append(portion)
            
        return "/" + "/".join(stack)



