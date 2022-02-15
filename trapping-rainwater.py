class Solution:
    def trap(self, height: List[int]) -> int:
        
        # O(n) time O(1) space
        # 2 pointers
        
        left, right = 0, len(height)-1
        output = 0
        maxHeight = 0
        
        while left < right:
            if height[left] < height[right]:
                if maxHeight - height[left] > 0:
                    output += maxHeight - height[left]
                maxHeight = max(maxHeight, height[left])
                left+=1
            else:
                if maxHeight - height[right] > 0:
                    output += maxHeight - height[right]
                maxHeight = max(maxHeight, height[right])
                right-=1
                
        return output 
