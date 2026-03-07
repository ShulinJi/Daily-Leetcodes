# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

 

# Example 1:


# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
# Example 2:


# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
# Example 3:

# Input: nestedList = [0]
# Output: 0
 

# Constraints:

# 1 <= nestedList.length <= 50
# The values of the integers in the nested list is in the range [-100, 100].
# The maximum depth of any integer is less than or equal to 50.



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# SECOND ATTEMPT
from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # we need to copy one by one because if we just use (nested, 1) the first element (nestedList) would be python list, not a nestedInteger list!!! will cause error when calling isInteger()

        # we can do this and another way is to use queue = deque(nestedList) so that we don't need to add depth as a tuple, it avoids the problem of first check is the python list.
        # then laster in the while loop, we need to find the length of each layer, for _ in range(len(queue)) to represent each layer, so that we can pop exactly that much node in current layer, then we increment the depth + 1 to indicate next layer.

        queue = deque([(element, 1) for element in nestedList])
        total = 0

        while queue:
            curr_element, curr_depth = queue.popleft()
            if curr_element.isInteger():
                total += curr_depth * curr_element.getInteger()
            else:
                for element in curr_element.getList():
                    queue.append((element, curr_depth + 1))
        
        return total


class Solution:
    # dfs, try to think how we find each list and go through all the element in the list
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(depth, curr_list):
            total = 0

            for element in curr_list:
                if element.isInteger():
                    total += element.getInteger() * depth
                else:
                    total += dfs(depth + 1, element.getList())
            
            return total
        
        return dfs(1, nestedList)



class Solution:
    # DFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_list, depth):
            # base case
            total = 0
            # for each list in the nested list, we check if it's an integer or a list
            for nest in nested_list:
                # If it's an integer, add it to the total multiplied by the depth
                # If it's a list, call dfs on that list with depth + 1 until we reach the base case
                if nest.isInteger():
                    total += nest.getInteger() * depth
                else:
                    total += dfs(nest.getList(), depth + 1)
            
            return total
        
        return dfs(nestedList, 1)

    # BFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)
        total = 0
        depth = 1
        while queue:
            # process all nodes at the current depth layer by layer
            for i in range(len(queue)):
                curr_node = queue.popleft()
                # If it's an integer, add it to the total multiplied by the depth
                # If it's a list, add all its elements to the queue to process at the next depth (layer)
                if curr_node.isInteger():
                    total += curr_node.getInteger() * depth
                else:
                    # extend the queue with all elements in the current list    
                    queue.extend(curr_node.getList())
            
            depth += 1
        
        return total

