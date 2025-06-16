# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        node_list = deque([root])
        ans = []

        while node_list:
            level_length = len(node_list)
            curr_level = []
            for i in range(level_length):
                node = node_list.popleft()
                curr_level.append(node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            ans.append(curr_level)
        
        return ans