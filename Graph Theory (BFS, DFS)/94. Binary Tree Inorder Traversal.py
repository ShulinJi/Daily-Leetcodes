# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# SECOND ATTEMPT
# O(n) because we traversed all of the nodes, and O(logn) avg because of how many function stacks but worst case is O(n) if examples like we tree does not have any branches
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder traversal: left, root, right, then we do the traversal in this order in dfs
        ans = []
        def dfs_traversal(node):
            # when we reach the end of the tree, we recurve back
            if not node:
                return 
            
            dfs_traversal(node.left)
            ans.append(node.val)
            dfs_traversal(node.right)

        dfs_traversal(root)
        return ans



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return_list = []
        def inorder(node):
            if node is not None:
                inorder(node.left)
                return_list.append(node.val)
                inorder(node.right)

        inorder(root)
        return return_list