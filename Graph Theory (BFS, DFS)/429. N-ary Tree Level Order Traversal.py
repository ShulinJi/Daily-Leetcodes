# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

# Constraints:

# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# O(n) and O(n) where n is the number of nodes in the tree
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        # use the bfs to traverse the tree
        queue = deque([root])
        ans = []

        while queue:
            # traverse the node layer by layer
            node_this_layer = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                node_this_layer.append(curr_node.val)
                # add all the children to the queue
                for child in curr_node.children:
                    # check if the child is None or are we at the leaf yet
                    if child:
                        queue.append(child)

            ans.append(node_this_layer)
        
        return ans



# How do we build the tree from the array?
    # [1,null,3,2,4,null,5,6]
    from collections import deque
    def buildTree(self, arr):
        # if array is None, then the root is None
        if not arr:
            return None
        
        # init the root value and children as empty list for future fill
        root = Node(arr[0], [])
        queue = deque(root)

        # i is the index for the array, we start at 2 b/c we have considered root = 1, and null (indicate end of the child)
        i = 2
        
        while i < len(arr) and queue:
            parent = queue.popleft()
            
            while i < len(arr) and arr[i] is not None:
                # create the new child and add to the children list
                new_child = Node(arr[i], [])
                parent.children.append(new_child)
                queue.append(new_child)
                i += 1
            
            # we reach here, we reach the null, need to skip it
            i += 1
        
        return root
