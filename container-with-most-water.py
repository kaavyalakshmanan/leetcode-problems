class Solution:
    def maxArea(self, height: List[int]) -> int:

        # O(n) time O(1) space
        # Sliding window
        
        left, right = 0, len(height)-1
        res = 0

        while left < right:
            currWidth = right-left
            currHeight = min(height[left], height[right])
            res = max(res, currWidth * currHeight)

            if height[left] <= height[right]:
                left+=1
            else:
                right-=1

        return res
