# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
 

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten_BST(self, node):
        # O(n) and O(n) space and time complexity
        if not node:
            return None
        if not node.left and not node.right:
            return node
        
        # pre-order traverse
        leftTail = self.flatten_BST(node.left)
        rightTail = self.flatten_BST(node.right)

        # attach the right subtree to left subtree
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        return rightTail if rightTail else leftTail
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_BST(root)


# O(1) space
class Solution:

    def flatten(self, root: TreeNode) -> None:
        # Handle the null scenario
        if not root:
            return None

        node = root
        while node:

            # If the node has a left child
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right
        