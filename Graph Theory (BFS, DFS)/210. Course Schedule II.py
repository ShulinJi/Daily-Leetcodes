# Exmaple of Topological Sort! (logical, follow the arrow, check the the arrows(dependencies) of a node and then check others)
# Simple Example
# Imagine you have a list of tasks to complete, but some tasks can’t be done until others are finished. For example:

# Tasks:

# Task A: Buy ingredients
# Task B: Cook dinner
# Task C: Set the table
# Task D: Eat dinner
# Dependencies:

# You can’t cook dinner (Task B) until you buy ingredients (Task A).
# You can’t set the table (Task C) until you’ve cooked dinner (Task B).
# You can’t eat dinner (Task D) until you’ve set the table (Task C).
# Order:

# The only way to do these tasks in the right order is: A → B → C → D
# This is topological sorting: arranging tasks so that all dependencies are respected.

# Key Idea
# Graph Representation:

# Tasks are like nodes.
# Dependencies are like arrows pointing from one task to another (e.g., "A → B" means "Do A before B").
# Topological Sort:

# It’s the process of finding an order to do all the tasks so that:
# No task is done before its prerequisites are complete.
# All tasks are completed in a valid order.




# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]


class Solution:
    # The three phase of a node, WHITE is not visited, GRAY is on stack, BLACK means its branch and neighbors are checked
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(x):
            # if we find a cycle, we simply just return
            nonlocal is_possible
            if is_possible == False:
                return

            # we set current node on stack
            color[x] = Solution.GRAY
            # Check for neighbors of current node
            if x in adj:
                for i in adj[x]:
                    # if the neighbor is on stack, it means we have a cycle
                    # else, we simply perform check
                    if color[i] == Solution.GRAY:
                        is_possible = False
                    elif color[i] == Solution.WHITE:
                        dfs(i)

            # we have checked the node and its branch and neighbors
            color[x] = Solution.BLACK
            # we append the topological order
            topological_sorted_order.append(x)


        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        # initialize k number of slot for each node
        color = {k: Solution.WHITE for k in range(numCourses)}
        topological_sorted_order = []
        is_possible = True
        for x in range(numCourses):
            # perform dfs if current node is not visited yet
            if color[x] == Solution.WHITE:
                dfs(x)
        
        # Return the topological order (reverse of stack)
        return topological_sorted_order[::-1] if is_possible else []
