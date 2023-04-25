class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]: 

        # O(n) time O(1) space

        i = lower
        res = []

        while i <= upper:
            for num in nums:
                if i == num:
                    i+=1
                else: 
                    res.append([i, num-1])
                    i = num+1

            if i <= upper:
                res.append([i, upper])
                i = upper+1

        return res

        
