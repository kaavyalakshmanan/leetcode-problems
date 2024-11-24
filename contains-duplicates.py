class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # O(n) time O(n) space
        # Hash set
        
        dupeSet = set()
        for num in nums:
            if num in dupeSet:
                return True
            dupeSet.add(num)

        return False
