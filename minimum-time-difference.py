class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        # O(nlogn) time, O(n) space
        
        for i, time in enumerate(timePoints):
            timeArr = time.split(":")
            hour, mins = int(timeArr[0]), int(timeArr[1])
            timePoints[i] = (hour * 60) + mins
         
        minTimeDiff = inf
        timePoints.sort()
        for i in range(len(timePoints)-1):
            time1, time2 = timePoints[i], timePoints[i+1]
            minTimeDiff = min(minTimeDiff, time2-time1)
        
        minTimeDiff = min(minTimeDiff, (timePoints[0] - timePoints[-1]) % 1440)
        
        return minTimeDiff
        
