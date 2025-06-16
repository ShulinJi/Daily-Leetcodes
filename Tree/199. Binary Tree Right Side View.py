# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:



# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        node_list = deque([root])

        while node_list:
            # number of nodes we need to pop so that we exactly pop the whole level of tree nodes
            # ex. 1st level: we already have root, which is 1, then we only need to pop one node
            # then we add 2 nodes, now level+lenght = 2, then we need to pop 2 nodes and then the second nodes is the rightest (ans)
            level_length = len(node_list)
            # pop the whole level
            for i in range(level_length):
                node = node_list.popleft()
                # the node we need
                if i == level_length - 1:
                    ans.append(node.val)
                
                # add the nodes for next level
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
        
        return ans
                
