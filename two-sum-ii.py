class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(n) time O(1) space
        # 2 pointers
        
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[right] + numbers[left] == target:
                return [left+1, right+1]
            elif numbers[right] + numbers[left] > target:
                right-=1
            else:
                left+=1
