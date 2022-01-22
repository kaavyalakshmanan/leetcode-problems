class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # O(n) time O(1) space
        # 2 pointers
        
        output = 0
        left, right = 0, len(height)-1
        while left < right:
            currWidth = right - left
            currHeight = min(height[left], height[right])
            output = max(output, currWidth * currHeight)
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        return output 
