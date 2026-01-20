# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) n is the number of nodes and O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def backtracking(curr_sum, node):
            nonlocal count
            if not node:
                return 
            
            curr_sum += node.val
            if curr_sum == targetSum:
                count += 1
            # we need this even when curr_sum == targetSum because there could be sum = 0
            count += prefix_sum_map[curr_sum - targetSum]

            prefix_sum_map[curr_sum] += 1
            backtracking(curr_sum, node.left)
            backtracking(curr_sum, node.right)
            prefix_sum_map[curr_sum] -= 1


        count = 0
        prefix_sum_map = defaultdict(int)
        backtracking(0, root)
        return count


# O(n) time complexity solution using DFS and a hashmap to store the frequency of prefix sums. O(h) space complexity, where h is the height of the tree.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        count = 0
        # we store the frequency of prefix sums
        # prefix sum: sums[i] = sum of node values from root to current node, like checkpoint in the path, whenever we reach a checkpoint
        # it's a new unqiue path that we can start counting from
        freq = {0: 1}

        def dfs(node, prefix_sum):
            nonlocal count

            if not node:
                return 
            
            # current prefix sum
            prefix_sum += node.val
            # see if there is a prefix sum that equals to prefix_sum - targetSum
            # if yes, then there is a path that sums to targetSum
            count += freq.get(prefix_sum - targetSum, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)
            # backtrack, remove the current prefix_sum from the map to avoid affecting other paths (branch)
            # we don't need to backtrack the prefix_sum itself as it's passed by value
            
            # In python, integers are immutable, so when we pass prefix_sum to the dfs function, we are passing a copy of the value, which stored on local stack
            # But the freq dictionary is mutable, so we need to backtrack it, stored on heap, shared among all function calls
            freq[prefix_sum] -= 1

        dfs(root, 0)
        return count
