class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        # O(nlogn) time O(n) space
        
        res = [0] * len(nums)
        
        for i, num in enumerate(nums):
            res[i] = (a * (num ** 2)) + (b * num) + c
            
        res.sort()
        return res
