class Solution:
    def trap(self, height: List[int]) -> int:

        # O(n) time O(1) space
        # 2 pointers
        
        left, right = 0, len(height)-1
        res, prevHeight = 0, 0
        while left < right:
            currHeight = min(height[left], height[right])
            if prevHeight - currHeight > 0:
                res += (prevHeight - currHeight)
            prevHeight = max(prevHeight, currHeight)

            if height[left] <= height[right]:
                left+=1
            else:
                right-=1

        return res
