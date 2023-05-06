class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        # we are allowed to sort the input array because the number of subsequences doesnt change regardless of whether input array is sorted or not

        # O(nlogn) time O(n) space

        nums.sort()
        res = 0
        mod = (10 ** 9) + 7

        # we want to see how many right values we can include for each subsequence starting at left
        right = len(nums)-1
        for left, num in enumerate(nums):
            while left <= right and nums[right] + nums[left] > target:
                right-=1
            if left <= right:
                res += (2 ** (right-left))
                res %= mod

        return res

        





        

