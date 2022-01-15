class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # O(n^2) time O(n) space
        # 3 pointers
        
        nums.sort()
        output = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            b, c = i+1, len(nums)-1
            while b < c:
                threeSum = a + nums[b] + nums[c]
                if threeSum < 0:
                    b+=1
                elif threeSum > 0:
                    c-=1
                else:
                    output.append([a, nums[b], nums[c]])
                    b+=1
                    c-=1
                    while b < c and nums[b] == nums[b-1]:
                        b+=1
                            
        return output 
