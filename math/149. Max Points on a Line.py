class Solution:
    # O(n^2) runtime and O(n) space
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[
                        math.atan2(
                            points[j][1] - points[i][1],
                            points[j][0] - points[i][0],
                        )
                    ] += 1
            result = max(result, max(cnt.values()) + 1)
        return result


# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

# In this example, three interesting lines contain the point (4,1) – the first line contains the points (4,1) and (5,3), the second one contains (4,1), (3,2), (2,3) and (1,4) and the third one contains (4,1) and (1,1). The angles between the X axis and the vectors from (4,1) to the points (3,2), (2,3) and (1,4) are equal (denoted with the green arc in the picture). In other words, all these vectors have the same atan2. On the other side, the vector from (4,1) to (5,3) has a different atan2 (denoted with the red arc). From this example, one can make the following observation:

# We call a point outside if it belongs to a line, but it doesn't lie between any other two points on this line (it's one of the edges). The vectors from an outside point to all other points on the line have the same atan2. Now the problem reduces to the following:

# For a fixed point points[i], consider all other points points[j] and calculate the atan2 for each vector points[j] - points[i] (the vector with the magnitudes (points[j].x - points[i].x, points[j].y - points[i].y)). Then find the maximum number of times some angle value occurs among the calculated values. One can use a hash map for this.

# Algorithm
# Iterate over all points. Let the current point be points[i]. Maintain a hash map cnt to count the angles.
# For each j
# 
# =i calculate the atan2 of the vector points[j] - points[i] and add this value to the hash map.
# Let k be the maximum number of occurrences of some angle value in the hash map.
# Update the answer with k+1. (+1 because the point points[i] also lies on the line, and we must include it in the answer.)
