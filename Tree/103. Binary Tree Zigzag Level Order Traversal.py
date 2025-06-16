# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        node_list = deque([root])

        # from left to right and from right to left, toggle it everytime 
        left_to_right = True
        ans = []

        while node_list:
            level_length = len(node_list)
            # record the order of nodes from left to right and based on left_to_right, we either reverse the list or keep the original
            curr_level = []
            for i in range(level_length):
                node = node_list.popleft()
                curr_level.append(node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            if left_to_right:
                ans.append(curr_level)
            else:
                curr_level.reverse()
                ans.append(curr_level)

            # toggle the left_to_right switch
            left_to_right = False if left_to_right == True else True
        
        return ans