class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(n) time O(1) space

        left, right = 0, len(numbers)-1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left+1, right+1]
            if currSum > target:
                right-=1
            else:
                left+=1
            
