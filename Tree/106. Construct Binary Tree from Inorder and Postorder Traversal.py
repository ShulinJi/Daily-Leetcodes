# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder left->root->right. postorder left->right->root preorder: root->left->right
        # postorder[-1] is the root
        def array_to_tree(left, right):
            # use inorder as a bound so that we can regulate when to stop
            if left > right:
                return None
            
            # from back to front b/c the order that the root is at the end
            root_value = postorder.pop()
            root = TreeNode(root_value)

            # construct right first b/c the order that we start from the back sot hat postorder: root->right-left
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right) 
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)

            return root
        
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        
        return array_to_tree(0, len(inorder) - 1)
