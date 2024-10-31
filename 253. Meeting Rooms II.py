# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        # Sort the meeting interval
        intervals.sort()
        # The meeting room that keeps the current meeting
        room = []
        for x in range(len(intervals)):
            current_meeting_start = intervals[x][0]
            # if current meeting start time is later than any of the meetings before, than we clear the room to be [] for other meetings to use (Don't need extra rooms)
            for y in range(len(room)):
                if room[y] != [] and room[y][1] <= current_meeting_start:
                    room[y] = []
            # Then we allocate the meeting to any available slot, if there's no slot, we just put it at the end (increase an room)
            if [] in room:
                for y in range(len(room)):
                    if room[y] == []:
                        room[y] = intervals[x]
                        break
            else:
                room.append(intervals[x])

        return len(room)


