class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # O(n) time O(1) space
        # 2 pointers
        
        left, right = 0, len(height)-1
        area = 0
        while left < right:
            currWidth = right - left
            currHeight = min(height[left], height[right])
            area = max(area, currWidth * currHeight)
            
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
                
        return area 
