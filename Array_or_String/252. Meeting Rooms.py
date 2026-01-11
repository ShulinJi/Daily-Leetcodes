# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106


# SECOND ATTEMPT
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # O(nlogn) and O(n) for python sort
        intervals.sort()

        for i in range(1, len(intervals)):
            # after sort based on the start time, if the start of the next interval is smaller than prev end time, then overlap
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        
        return True


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Brute force approcach, too slow
        # left_bound = 0
        # right_bound = 0
        
        # for x in range(len(intervals)):
        #     for y in range(len(intervals)):
        #         if y != x:
        #             if (intervals[x][0] == intervals[y][0]) and (intervals[y][1] == intervals[x][1]):
        #                 return False
        #             if (intervals[x][0] < intervals[y][0] < intervals[x][1]) or (intervals[x][0] < intervals[y][1] < intervals[x][1]):
        #                 return False
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        
        return True

        # OR

        intervals.sort()
        for x in range(len(intervals) - 1):
            if intervals[x][1] > intervals[x + 1][0]:
                return False
        return True
