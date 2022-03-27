class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        # O(n) time O(1) space
        # Monotonic stack with space optimization
        
        length = len(heights)-1
        output = [length]
        maxHeight = heights[length]
        
        for i in range(length-1, -1, -1):
            currHeight = heights[i]
            if currHeight > maxHeight:
                output.append(i)
                maxHeight = currHeight
        
        return output[::-1]
