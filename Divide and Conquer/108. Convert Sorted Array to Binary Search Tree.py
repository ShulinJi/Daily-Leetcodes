Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: If the array is empty, return None
        if not nums:
            return None
        
        # Find the middle element of the array
        mid = len(nums) // 2
        
        # Create the root node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively construct the left subtree using the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively construct the right subtree using the right half of the array
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root



# Divide and Conquer:

# For a height-balanced BST, the middle element of the array becomes the root.
# The elements to the left of the middle form the left subtree.
# The elements to the right of the middle form the right subtree.
# Base Case:

# If the array is empty (nums == []), return None.
# Recursive Calls:

# The function recursively splits the array into smaller subarrays until it reaches individual elements, which become leaf nodes in the BST.

# Execution:
# The array [-10, -3, 0, 5, 9] is split at mid = 2:

# Root: TreeNode(0)
# Left subtree: [-10, -3]
# Right subtree: [5, 9]
# The left subtree [-10, -3] is split at mid = 1:

# Root: TreeNode(-3)
# Left subtree: [-10]
# Right subtree: []
# The left subtree [-10] becomes a leaf node:

# Root: TreeNode(-10)
# Left: None
# Right: None
# The right subtree [5, 9] is split at mid = 1:

# Root: TreeNode(9)
# Left subtree: [5]
# Right subtree: []
# The left subtree [5] becomes a leaf node:

# Root: TreeNode(5)
# Left: None
# Right: None