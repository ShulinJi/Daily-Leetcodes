class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs_back_track(start, end, product, visited):
            visited.add(start)
            ret = -1
            # get all the connected neighbors from the graph
            neighbors = graph[start]
            if end in neighbors:
                # if our end node is our neighbor
                return product * neighbors[end]
            else:
                # need the .item() to get key value pair since neighbors is a dictionary
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = dfs_back_track(neighbor, end, product * value, visited)
                    # it means we have found our answer, else it'll be -1
                    if ret != -1:
                        break
            visited.remove(start)
            return ret

        # initialize a nested disctionary for the graph
        graph = defaultdict(defaultdict)

        # fill in the graph with edge value
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        result = []
        for dividend, divisor in queries:
            # if one of the dividend or divisor not in graph, could not find
            if dividend not in graph or divisor not in graph:
                ret = -1
            # if dividend and divisor are the same
            elif dividend == divisor:
                ret = 1
            else:
                visited = set()
                ret = dfs_back_track(dividend, divisor, 1, visited)
            result.append(ret)
        return result




# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
