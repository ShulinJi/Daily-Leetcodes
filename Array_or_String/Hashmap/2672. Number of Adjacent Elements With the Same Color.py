# You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

# Set colors[indexi] to colori.
# Count the number of adjacent pairs in colors which have the same color (regardless of colori).
# Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

 

# Example 1:

# Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

# Output: [0,1,1,0,2]

# Explanation:

# Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.
# After the 1st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.
# After the 2nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.
# After the 3rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.
# After the 4th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.
# After the 5th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.
# Example 2:

# Input: n = 1, queries = [[0,100000]]

# Output: [0]

# Explanation:

# After the 1st query colors = [100000]. The count of adjacent pairs with the same color is 0.

 

# Constraints:

# 1 <= n <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= indexi <= n - 1
# 1 <=  colori <= 105


# Time: O(q)
# Space: O(lenghth) space because we preallocate that much, but if n gets too big, it will fail the space complexity
from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        color = [0] * n
        # we are counting the number of adjacent pairs with the same color, so we can just keep track of that number and update it as we go through the queries
        pairs = 0
        ans = []

        for coor, new_color in queries:
            old_color = color[coor]
            # if old color is same as new color, then we don't need to update anything, just append the current number of pairs to the answer
            if old_color == new_color:
                ans.append(pairs)
                continue
            # if old color is not 0, then we need to check if we break or form any pairs with the old color, and update the pairs count accordingly
            if old_color != 0:
                # if we break any adjacent pairs with the old color, we need to decrease the pairs count by 1 for each pair we break
                if coor - 1 >= 0 and color[coor - 1] == old_color:
                    pairs -= 1
                if coor + 1 < n and color[coor + 1] == old_color:
                    pairs -= 1

            # then we add new color and see if we form any new pairs with the new color, and update the pairs count accordingly
            color[coor] = new_color

            if new_color != 0:
                if coor - 1 >= 0 and color[coor - 1] == new_color:
                    pairs += 1
                if coor + 1 < n and color[coor + 1] == new_color:
                    pairs += 1

            ans.append(pairs)

        return ans