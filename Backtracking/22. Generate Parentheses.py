# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# Brute Force Solution
# Time complexity: O(2*2n⋅n) same for space complexity
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # check for the validation of each string
        def check_valid_parentheses(s):
            balance = 0
            for x in s:
                if balance < 0:
                    return False
                if x == "(":
                    balance += 1
                elif x == ")":
                    balance -= 1

            return True if balance == 0 else False
        
        # Generate each possible string
        def backtrack(curr):
            if len(curr) == n * 2:
                if check_valid_parentheses(curr):
                    ans.append("".join(curr))
                return
            
            for char in "()":
                curr.append(char)
                backtrack(curr)
                curr.pop()
            
        backtrack([])
        return ans