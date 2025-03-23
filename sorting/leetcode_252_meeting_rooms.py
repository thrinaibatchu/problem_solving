class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if (intervals[i][0] >= intervals[j][0] and intervals[i][0] < intervals[j][1] or intervals[j][0] >= intervals[i][0] and intervals[j][0] < intervals[i][1]):
                    return False
        
        return True