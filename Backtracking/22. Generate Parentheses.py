# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# SECOND ATTEMPT
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(curr_string, left_count, right_count):
            if len(curr_string) == 2 * n:
                ans.append("".join(curr_string))
            
            if left_count < n:
                curr_string.append("(")
                left_count += 1
                backtracking(curr_string, left_count, right_count)
                left_count -= 1
                curr_string.pop()
            
            if right_count < left_count:
                curr_string.append(")")
                right_count += 1
                backtracking(curr_string, left_count, right_count)
                right_count -= 1
                curr_string.pop()
        
        backtracking([], 0, 0)
        return ans

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

# more optimal solution that eliminates invalid string check
# Time complexity (4^n / sqrt(n)), space complecity O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            # if left_count is < n, it means we could still add "(" to the string
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            # if right is < left, it means we could add ")" to our string
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()

        backtracking([], 0, 0)
        return answer
