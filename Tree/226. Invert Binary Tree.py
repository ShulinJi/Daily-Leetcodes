# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = collections.deque([root])
        while queue:
            # keep poping the queue
            current = queue.popleft()
            # we swap the left and right child recursively
            current.left, current.right = current.right, current.left
            
            # we add left side to the queue if not None
            if current.left:
                queue.append(current.left)
            
            # we add right side to the queue if not none
            if current.right:
                queue.append(current.right)
        
        return root

# my recursion solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # python always pass by reference!
        self.invert_tree(root)
        return root
    def invert_tree(self, node):
        if not node:
            return 
        if not node.left and not node.right:
            return 
        
        self.invertTree(node.left)
        self.invertTree(node.right)

        node.left, node.right = node.right, node.left
        return