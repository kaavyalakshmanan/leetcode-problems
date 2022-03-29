class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        # O(n) time O(1) space
        
        output = [len(heights)-1]
        maxHeight = heights[-1]
        
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                output.append(i)
                
                
        return output[::-1]
        
