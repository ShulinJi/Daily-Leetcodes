# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p, q])
        while queue:
            p = queue.popleft()
            q = queue.popleft()

            if not p and not q:
                continue
            
            if not p or not q or p.val != q.val:
                return False

            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True



# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Input: p = [1,2], q = [1,null,2]
# Output: false
