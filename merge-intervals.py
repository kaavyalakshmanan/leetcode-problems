class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # O(nlogn) time O(n) space
        
        intervals.sort()
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            prevStart, prevEnd = output[-1]
            if start >= prevStart and start <= prevEnd:
                output[-1][1] = max(prevEnd,  end)
            else:
                output.append([start, end])
        return output 
        
