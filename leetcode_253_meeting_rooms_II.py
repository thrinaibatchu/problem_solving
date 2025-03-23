class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        rooms = []  # Min-heap to store end times of meetings in rooms
        heapq.heappush(rooms, intervals[0][1])  # Add the end time of the first meeting

        for i in range(1, len(intervals)):
            start_time = intervals[i][0]
            end_time = intervals[i][1]

            if start_time >= rooms[0]:  # If the current meeting starts after the earliest ending meeting
                heapq.heapreplace(rooms, end_time)  # Reuse the room
            else:
                heapq.heappush(rooms, end_time)  # Allocate a new room

        return len(rooms)