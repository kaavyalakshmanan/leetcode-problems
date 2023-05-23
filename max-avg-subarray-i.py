class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # O(n) time O(1) space

        left, right = 0, 0
        prefixSum = 0
        while right < len(nums) and (right-left+1) < k:
            prefixSum += nums[right]
            right+=1

        res = -inf
        
        while right < len(nums):
            prefixSum+=nums[right]
            res = max(prefixSum/k, res)
            prefixSum-=nums[left]
            left+=1
            right+=1

        return res

        
