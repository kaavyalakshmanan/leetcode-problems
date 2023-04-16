class Solution:
    def trap(self, height: List[int]) -> int:

        # O(n) time O(1) space

        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        res = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            currRes = min(leftMax, rightMax) - min(height[left], height[right])
            if currRes > 0:
                res += currRes
            
            if leftMax <= rightMax:
                left+=1
            else:
                right-=1

        return res


        
