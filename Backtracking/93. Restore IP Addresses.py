# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 1 <= s.length <= 20
# s consists of digits only.


# Backtracking patterns
def backtrack(state):
    if is_goal(state):
        record_solution(state)
        return

    for choice in choices(state):
        if is_valid(choice):
            make_choice(state, choice)
            backtrack(state)
            undo_choice(state, choice)

# SECOND ATTEMPT
# O(m^n * n) m is 3, n is 4, so we have a O(1) time complexity, 3^4 to find all possible segments, n to copy
# O(m * n) since max length of path is 3 * 4 + 3 dots, so O(1)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtracking(curr_index, path):
            # if we have 4 segments and we are at len(s) -> trversed all the string
            if len(path) == 4:
                if curr_index == len(s):
                    ans.append(".".join(path[:]))
                # if we have 4 segments and have not reached the end or over the end, return
                return

            for i in range(1, 4):
                # if bigger than len(s), then we cannot s[:curr + i] out of bound, but curr+i == len(s) i sstill valid
                if curr_index + i > len(s):
                    return
                curr_segment = s[curr_index: curr_index + i]
                # if all digits are integer
                for digit in curr_segment:
                    if not digit.isdigit():
                        return
                # if have leading zero or bigger thn 255
                if len(curr_segment) > 1 and int(curr_segment[0]) == 0:
                    return 
                if int(curr_segment) > 255:
                    return

                # then we start to backtracking again
                path.append(curr_segment)
                backtracking(curr_index + i, path)
                path.pop()
            
        ans = []
        backtracking(0, [])
        return ans


# Personal Solution
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        ans = set()
        def backtracking(dot_count, ip, ip_segment, rest_string):
            # if there is still string left but used all 3 dots
            if dot_count == 4 and len(ip_segment):
                return
            # if there is still dots and we used up all the segments
            elif dot_count != 4 and len(ip_segment) == 0:
                return 
                
            # if the digits is not number
            for x in ip_segment:
                if not x.isdigit():
                    return
            # contain leading zero
            if  len(ip_segment) > 1:
                if int(ip_segment[0]) == 0:
                    return 
                # if ip segment is bigger than 255
                if int(ip_segment) > 255:
                    return 

            if dot_count == 4:
                ans.add("".join(ip))
                return 

            dot_count += 1
            ip.append(ip_segment)
            ip.append(".")
            for x in range(1, 4):
                backtracking(dot_count, ip, rest_string[0:x], rest_string[x:])
            ip.pop()
            ip.pop()
            dot_count -= 1
            # pop the dot and the last ip_segment we tried

        # starting with first 3 element
        for x in range(1, 4):
            backtracking(0, [], s[0:x], s[x:])
        
        ans = list(ans)
        for x in range(len(ans)):
            ans[x] = "".join(ans[x])
            ans[x] = ans[x][:-1]
        
        return ans




# GPT Answer, much cleaner!

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start: int, path: List[str]):
            # 🛑 Base case: 4 segments and no chars left
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            
            # ✂️ Try 1 to 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break  # Out of bounds

                segment = s[start:start+length]

                # 🚫 Skip invalid segments
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue

                # ✅ Recurse with this segment added
                backtrack(start + length, path + [segment])

        # 🚀 Start backtracking
        backtrack(0, [])

        return result
        
