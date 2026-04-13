# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1
 

 

# Constraints:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106

# SECOND ATTEMPT
# O(N) where N is the total number of stops in all routes, since we will visit each stop at most once.
# O(N) space for the queue and the seen sets. In the worst case, we might have to store all stops in the queue and seen sets.
from collections import deque
from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_route = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].add(i)
        
        seenRoutes = set()
        seenStop = {source}

        queue = deque([(source, 0)])
        while queue:
            stop, count = queue.popleft()
            if stop == target:
                return count

            for route_id in stop_to_route[stop]:
                if route_id not in seenRoutes:
                    seenRoutes.add(route_id)
                    for stop in routes[route_id]:
                        if stop not in seenStop:
                            seenStop.add(stop)
                            queue.append((stop, count + 1))
        
        return -1

class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stopToRoute = collections.defaultdict(set)
        
        for i, stops in enumerate(routes):
            for stop in stops: 
                stopToRoute[stop].add(i)
                
        bfs = [(S,0)]
        seenStops = {S}
        seenRoutes = set()
        
        for stop, count in bfs:
            if stop == T: 
                return count
            
            for routeIndex in stopToRoute[stop]:
                if routeIndex not in seenRoutes:
                    seenRoutes.add(routeIndex)
                    for next_stop in routes[routeIndex]:
                        if next_stop not in seenStops:
                            seenStops.add(next_stop)
                            bfs.append((next_stop, count+1))
        return -1