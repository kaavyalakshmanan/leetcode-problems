class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # O(n) time O(1) space
        
        output = []
        mergeStart, mergeEnd = newInterval
        
        for i, (start, end) in enumerate(intervals):
            # Overlap
            if (start <= mergeEnd or and start <= mergeEnd) or (end >= mergeStart and end <= mergeEnd) or (mergeStart >= start and mergeStart <= end) or (mergeEnd >= start and mergeEnd <= end):
                mergeStart = min(mergeStart, start)
                mergeEnd = max(mergeEnd, end)
            else:
                if end < mergeStart:
                    output.append([start, end])
                else:
                    output.append([mergeStart, mergeEnd])
                    # if i == len(intervals)-1:
                    mergeStart, mergeEnd = start, end
                
        output.append([mergeStart, mergeEnd])
        return output 
        
        
