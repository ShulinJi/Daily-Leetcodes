# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        meeting_rooms = []

        # push the end time of the meeting
        heapq.heappush(meeting_rooms, intervals[0][1])
        min_length = 0

        # if len of intervals is 1, then just need 1 meeting room
        if len(intervals) == 1:
            return 1
            
        # if we have a meeting that happens after the head of min heap, then we have an empty meeting room
        for meeting in intervals[1:]:
            if meeting[0] >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            # add current meeting end time to the heap
            heapq.heappush(meeting_rooms, meeting[1])
            # update the length of min number of meeting rooms we need
            min_length = max(min_length, len(meeting_rooms))   

        return min_length



##### Equavalent solution

        class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
