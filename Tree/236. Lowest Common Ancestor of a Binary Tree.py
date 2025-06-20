# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n) and O(n)
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestor(node):
            if not node:
                return False
            
            # if left, right, mid, any 2 of three are True, it menas we find the lowest common ancestor b/c the current node has p, q on different subtree 
            # or including itself(mid)
            left = findAncestor(node.left)
            right = findAncestor(node.right)
            
            # if current node equals to p or q, then we found a node already (mid)
            mid = True if node == p or node == q else False
            if mid + left + right == 2:
                self.ans = node
            
            # return True if any of these are True
            return mid or left or right
        findAncestor(root)
        return self.ans
