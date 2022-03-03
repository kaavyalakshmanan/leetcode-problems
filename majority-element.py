class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # O(n) time O(n) space
        # HashMap
        
        count = {}
        maxCount, maxVal = 0, 0
        
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
            if count[num] > maxCount:
                maxCount = count[num]
                maxVal = num
            
        return maxVal 
    
        # O(n) time O(1) space
        # Boyer Moore Algo
        
        count, res = 0, 0
        for num in nums:
            if count == 0 and num != res:
                res = num
                count+=1
            elif num == res:
                count+=1
            else:
                count-=1
                
        return res
            
            
