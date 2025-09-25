# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Example 2:


# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Example 3:


# Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
# Output: [[4],[2,5],[1,10,9,6],[3],[11]]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # min and max column indices to know the range of columns so that we don't have to sort the keys of the dictionary at the end
        min_col = 0
        max_col = 0
        queue = deque([(root, 0)])
        # store the nodes in each column, key is the column index, value is a list of node values in that column
        column = defaultdict(list)
        column[0].append(root.val)

        while queue:
            # BFS
            curr_node, col = queue.popleft()
            # update the min and max column indices
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            # check if left and right children exist, if they do, add them to the queue with their corresponding column index
            if curr_node.left:
                column[col - 1].append(curr_node.left.val)
                queue.append((curr_node.left, col - 1))
            if curr_node.right:
                column[col + 1].append(curr_node.right.val)
                queue.append((curr_node.right, col + 1))

        return [column[x] for x in range(min_col, max_col + 1)]
