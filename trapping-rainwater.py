class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Algo: 2 pointer
        # keep track of maxLeft and maxRight
        # current val = min(left, right)
        # current amount trapped = min(maxLeft, maxRight) - current val
        # move the pointer pointing to smaller val

        # O(n) time O(1) space

        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]
        res = 0

        while left < right:
            currentVal = min(height[left], height[right])
            currentAmt = min(maxLeft, maxRight) - currentVal
            if currentAmt > 0:
                res += currentAmt
            if height[left] <= height[right]:
                left+=1
                maxLeft = max(maxLeft, height[left])
            else:
                right-=1
                maxRight = max(maxRight, height[right])

        return res
