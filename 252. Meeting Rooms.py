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

        intervals.sort()
        for x in range(len(intervals) - 1):
            if intervals[x][1] > intervals[x + 1][0]:
                return False
        return True
