class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # O(n * sum(nums)) time O(sum(nums)) space
        # DP
        
        if sum(nums) % 2 == 1:
            return False
        
        numsSet = set()
        numsSet.add(0)
        target = sum(nums)/2
        
        for i in range(len(nums)):
            currNum = nums[i]
            tempSet = set()
            for t in numsSet:
                tempSet.add(currNum + t)
                tempSet.add(t)
            numsSet = tempSet
                
            
        
        return target in numsSet
