class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # O(n^2) time O(n) space
        # reduce problem to 2 sum 2
        
        nums = sorted(nums)
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            b, c = i+1, len(nums)-1
            while b < c:
                threeSum = a + nums[b] + nums[c]
                if threeSum == 0:
                    res.append([a, nums[b], nums[c]])
                    b+=1

                    while b < c and nums[b] == nums[b-1]:
                        b+=1
                
                elif threeSum < 0:
                    b+=1
                else:
                    c-=1

        return res
