class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # O(n) time O(1) space
        
        left, right = 0, 0
        zeroPtr, zeroCount  = 0, 0
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroCount+=1

                if zeroCount == 1:
                    zeroPtr = right
                else:
                    res = max(res, right-left-1)
                    left = zeroPtr+1
                    zeroPtr = right
                    zeroCount = 1

            elif right == len(nums)-1:
                res = max(res, right-left)

                
            right+=1

        return res
