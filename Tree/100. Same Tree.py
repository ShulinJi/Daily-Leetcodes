# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use dequeue because it has both O(1) for pop from left and O(1) for pop from right
        queue = deque([p, q])
        while queue:
            # pop first two elements
            p = queue.popleft()
            q = queue.popleft()

            # If both of the values are None, we continue checking
            if not p and not q:
                continue
            
            # if values are different, then return False
            # if one of them is None, and other is not (we have covered case when both are None),
            # then structure is different
            if not p or not q or p.val != q.val:
                return False

            # we add both left sides and right sides to the queue
            # as a result, we are checking the BFS left side first, after checking all of the left tree
            # then we start checking the whole right tree
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
