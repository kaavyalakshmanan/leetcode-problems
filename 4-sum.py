class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        # O(n^3) time O(n) space

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                b = nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    c, d = nums[left], nums[right]
                    currSum = a + b + c + d
                    if currSum == target:
                        res.append([a, b, c, d])
                        left+=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                    elif currSum < target:
                        left+=1
                    else: right-=1

        return res

                    
