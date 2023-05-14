class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # prefix sums 
        # O(n) time O(1) space
        
        left, right = 0, 0
        prefixSum, length = 0, inf

        while right < len(nums):
            prefixSum += nums[right]
            while prefixSum >= target:
                length = min(length, right-left+1)
                prefixSum-=nums[left]
                if left == right:
                    right+=1
                left+=1
            right+=1

        return length if length != inf else 0


