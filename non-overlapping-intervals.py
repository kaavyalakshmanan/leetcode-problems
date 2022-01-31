class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # O(nlogn) time O(n) space
        # Greedy
        
        intervals.sort()
        s1, e1 = intervals[0]
        output = 0
        i = 1
        while i < len(intervals):
            s2, e2 = intervals[i]
            # Check if there is overlap
            if s2 < e1:
                # Get rid of interval that ends later
                    output+=1
                    if e1 > e2:
                        s1, e1 = s2, e2
            else:
                s1, e1 = s2, e2
            i+=1
        
        return output
            
