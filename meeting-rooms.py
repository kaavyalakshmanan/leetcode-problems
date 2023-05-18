class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # O(nlogn) time O(n) space

        if not intervals:
            return True

        intervals.sort()
        prevStart, prevEnd = intervals[0][0], intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevStart and start < prevEnd:
                return False
            prevStart, prevEnd = start, end

        return True


