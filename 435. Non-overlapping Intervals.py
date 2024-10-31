class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on the end time, prioritize intervals that finish early
        intervals.sort(key=lambda x: x[1])

        # prev stores the last non-overlapping intervals
        prev = intervals[0]
        # length of how many maximum non-overlapping intervals
        count = 1

        for x in range(1, len(intervals)):
            if intervals[x][0] >= prev[1]:
                count += 1
                prev = intervals[x]
        
        return len(intervals) - count




# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
