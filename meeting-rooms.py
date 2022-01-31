class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if not intervals:
            return True
        
        intervals.sort()
        s1, e1 = intervals[0]
        i = 1
        
        while i < len(intervals):
            s2, e2 = intervals[i]
            if s2 < e1:
                return False
            s1, e1 = s2, e2
            i+=1
        
        return True
        
