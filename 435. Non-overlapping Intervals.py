class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prev = intervals[0]
        count = 1

        for x in range(1, len(intervals)):
            if intervals[x][0] >= prev[1]:
                count += 1
                prev = intervals[x]

        return len(intervals) - count
