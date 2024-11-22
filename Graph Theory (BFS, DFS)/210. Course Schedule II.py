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
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(x):
            nonlocal is_possible
            if is_possible == False:
                return
            color[x] = Solution.GRAY
            if x in adj:
                for i in adj[x]:
                    if color[i] == Solution.GRAY:
                        is_possible = False
                    elif color[i] == Solution.WHITE:
                        dfs(i)
            color[x] = Solution.BLACK
            topological_sorted_order.append(x)


        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        # initialize k number of slot for each node
        color = {k: Solution.WHITE for k in range(numCourses)}
        topological_sorted_order = []
        is_possible = True
        for x in range(numCourses):
            if color[x] == Solution.WHITE:
                dfs(x)
        
        # Return the topological order (reverse of stack)
        return topological_sorted_order[::-1] if is_possible else []
