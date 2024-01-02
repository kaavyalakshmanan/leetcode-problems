class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # O(n) time O(n) space
        # Use hash set
        
        numsSet = set()
        for num in nums:
            if num not in numsSet:
                numsSet.add(num)
            else:
                return True

        return False
