# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n^2) time, O(h) space, h is the height of the tree
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ans = []
        def findPath(node, curr_path):
            # not a leaf node, just ignore
            if node is None:
                return 

            # we find a leaf node
            if node.left is None and node.right is None:
                curr_path.append(node.val)
                print(curr_path)
                curr_sum = sum(curr_path)
                if curr_sum == targetSum:
                    ans.append(list(curr_path))
                curr_path.pop()
                return 
            
            # not a leaf node, continue the search
            curr_path.append(node.val)
            findPath(node.left, curr_path)
            findPath(node.right, curr_path)
            # backtrack
            curr_path.pop()

        findPath(root, [])
        return ans
