# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

# Example 1:

# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:

# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
 

# Constraints:

# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, avails):
        BEGIN, END = 0, 1

        # intervals are events (begin, end) when it begins we add 1 to the total number of person (bal)
        # when we see end, we -1 from the bal (total number of working people)
        # if we see a bal == 0, it means that we have a total of 0 people are working right now, 
        # so it is a free time
        events = []
        for employee in avails:
            for interval in employee:
                events.append((interval.start, BEGIN))
                events.append((interval.end, END))
        events.sort()

        ans = []
        prev = None
        balance = 0

        # sweep through the time intervals and 
        for time, action in events:
            # whenever we see a balance of 0, we add interval [prev, current_time], current_time must be BEGIN
            if balance == 0 and prev is not None:
                ans.append(Interval(prev, time))

            balance += 1 if action is BEGIN else -1
            prev = time

        return ans