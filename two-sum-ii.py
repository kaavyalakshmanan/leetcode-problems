class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(n) time O(1) space
        # 2 pointers
        
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] < target:
                left+=1
            else:
                right-=1
            
