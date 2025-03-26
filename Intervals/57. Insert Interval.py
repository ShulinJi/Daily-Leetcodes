class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # (O(logn + N)) => O(n)
        # Binary search to find where to insert the interval
        low, high = 0, len(intervals) - 1
        while low <= high:
            mid = (low + high) // 2
            if intervals[mid][0] <= newInterval[0]:
                low = mid + 1
            else:
                high = mid - 1

        # insert the new interval
        intervals.insert(low, newInterval)
        # merge the interval

        merge = []
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(interval[1], merge[-1][1])
        return merge




        # O(nlogn)
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            # new interval does not overlap with the last interval, we simply just insert the intervals
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # if there's a overlap, we just update the last interval so that the maximum is the max between new interval and last interval, 
                # so that we are basically merging the interval
                merged[-1][1] = max(interval[1], merged[-1][1])
                
        return merged



# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
