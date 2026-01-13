
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
      
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
      
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# SECOND ATTEMPT, O(nlogn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on the first index
        intervals.sort()
        merged = []

        for interval in intervals:
            # the two interval does not overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # the two overlap, then we decide how to merge, since the left is 100% the merged[-1][0] because sorted
                # then we only need yo merge the max of right side
                merged[-1][1] = max(interval[1], merged[-1][1]) 
                # new_interval = [merged[-1][0], max(interval[1], merged[-1][1])]
                # merged[-1] = new_interval
        
        return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # If merged is empty or there's no overlap, add the current interval, no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, merge the current interval with the last interval in merged
                # merged[-1][1] >= interval[0] => there is overlap
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
