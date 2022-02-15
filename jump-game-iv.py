class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left, right = 0, 0
        output = 0
        
        while right < len(nums)-1:
            jumpDist = 0
            for i in range(left, right+1):
                jumpDist = max(jumpDist, nums[i]+i)
            output+=1
            left = right+1
            right = jumpDist
            
        return output 
            
