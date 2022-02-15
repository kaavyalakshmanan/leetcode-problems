class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # O(n*n!) time O(n) space
        # Backtracking 
        
        if len(nums) == 1:
            return [nums[:]]
        
        output = []
        
        for i in range(len(nums)):
            num = nums.pop(0)
            
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
                
            output.extend(perms)
            nums.append(num)
            
        return output 
        
