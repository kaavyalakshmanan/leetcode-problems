class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # O(nlogn) time O(n) space because sorting

        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prevStart, prevEnd = res[-1]
            if start >= prevStart and start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])

        return res
