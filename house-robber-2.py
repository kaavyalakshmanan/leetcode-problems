class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # O(n) time O(1) space
        # Reduce to HR1
        
        def houseRobber(nums, maxAmount):
            maxAmount = max(nums[-1], nums[-2])
            for i in range(len(nums)-3, -1, -1):
                second = nums[i] + nums[i+2]
                third = nums[i] + nums[i+3] if i+3 < len(nums) else 0
                nums[i] = max(second, third)
                maxAmount = max(maxAmount, nums[i])

            return maxAmount
        
        if len(nums) == 1:
            return nums[0]
        maxAmount = max(nums[-1], nums[-2])
        if len(nums) == 2:
            return maxAmount
        
        first = houseRobber(nums[1:], maxAmount) 
        second = houseRobber(nums[:-1], maxAmount)
        
        return max(first, second)
