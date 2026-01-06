# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

# Example 1:

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:

# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the children, 
# You need to output 2.
 

# Constraints:

# 1 <= g.length <= 3 * 104
# 0 <= s.length <= 3 * 104
# 1 <= g[i], s[j] <= 231 - 1
 

# Note: This question is the same as 2410: Maximum Matching of Players With Trainers.

# SECOND ATTEMPT
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # first sort to ensure the two pointer approach
        # O(nlogn)
        g.sort()
        s.sort()

        # two pointer for each array
        p1 = 0
        p2 = 0

        ans = 0
        while p1 < len(g) and p2 < len(s):
            # if the greedy factor has been met, then +1 for the child list
            if g[p1] <= s[p2]:
                ans += 1
                p1 += 1
            # either met or not met, we both need to add p2 for next cookie
            p2 += 1

        return ans


# O(n log n) time and O(n) space with sorting and two pointers
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:
            return 0

        # Sort both arrays and use two pointers to find the maximum number of content children
        g.sort()
        s.sort()

        # p1 points to the greed factor array, p2 points to the size array
        p1 = 0
        p2 = 0

        # If the size of the cookie is greater than or equal to the greed factor of the child, we can assign the cookie to the child
        # and move both pointers to the next child and the next cookie and stop as soon as we reach the end of either array
        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        
        # return p1, which is the number of content children
        return p1
