# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# DFS Solution, Runtime O(M+N), Space O(M+N)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS to find if there's a cycle in the graph by finding if the node on recursion stack is the one we are checking
        # Also, we track visited, if we have visited the node, we continue to the next
        def dfs(course_number, adj, visited, inStack):
            # If the node we are checking is on stack, we have a cycle
            if inStack[course_number] == True:
                return True
            # if the node we have already checked, we continue
            if visited[course_number] == True:
                return False
            
            # Set the current node to stack and visited
            visited[course_number] = True
            inStack[course_number] = True
            # Check the branch of the node if there's any cycle in it
            # If so, return True, we find a cycle 
            for course in adj[course_number]:
                if dfs(course, adj, visited, inStack):
                    return True
            
            # We remove the current node from the stack since we finished checking its branch
            inStack[course_number] = False
            return False


        # add number of [] with nuber of courses
        # index represents the course number and content represents its prerequisite courses
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
        
        # Create visited and inStack for DFS use
        # Visited: track the node we have visited
        # inStack: track the DFS recursion stack, if the node is on Stack, we make it True
        visited = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            # If there is a cycle in a graph, we return False
            if dfs(i, adj, visited, inStack):
                return False
        return True
