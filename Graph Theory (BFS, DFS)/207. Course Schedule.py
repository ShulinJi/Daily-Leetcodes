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

# SECOND ATTEMPT
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(V + E) because each node and edges are at most processed once because of visited array, adj cost O(E), 
        # and the dfs cost O(V + E)
        # space: O(V + E), adj cost O(E) which is the length of prerequisites, and then visted and instack cost O(V)
        def dfs(course_num, visited, inStack):
            # if current on stack, we have a cycle, cannot take all courses, return true(have a cycle)
            if inStack[course_num]:
                return True
            
            # if we have previously checked this branch and it is safe in previous dfs calls, we knows we can skip
            if visited[course_num]:
                return False
            # add current course to the stack
            inStack[course_num] = True

            # check the prerequisite and continue expand the branches back to front
            for course in adj[course_num]:
                if dfs(course, visited, inStack):
                    return True
            
            # we finished checking, and this branch is safe and no cycle is found here
            # we pop the current_course from stack and add it to the safe visited
            inStack[course_num] = False
            visited[course_num] = True

            return False


        # we create a list of course prerequisite, the index represents the course number from 0 to numCourse - 1
        # and its value represents the prerequisite required to take this course
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        # both are global even though they are paseed to functions, but lists they are mutable, and python will
        # pass the reference to the same mutable!
        # visited is used to keep track of the branches we hav already checked and can prune early
        # instack is used to keep track of current path and backtrack it after checking one whole branch
        # can also use a set to replace inStack, then we use add, remove, equivalent
        visited = [False] * numCourses
        inStack = [False] * numCourses

        for i in range(numCourses):
            # if any of the dfs finds a cycle: instack == true, we cannot take all courses
            if dfs(i, visited, inStack):
                return False
        
        return True

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


        # add number of [] with number of courses
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
