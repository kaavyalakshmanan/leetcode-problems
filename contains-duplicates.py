class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # O(n) time O(n) space
        # One pass hash
        
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False
