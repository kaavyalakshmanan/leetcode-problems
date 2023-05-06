class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        # in this problem we want to determine if input array can be converted to non-decreasing array with at most one change
        # so we want to keep track of whether more than one change is required -- in which case we would return False
        # we iterate over the array and for every element we keep track of whats on the left and whats on the right
        # if curr element is > right, we check whether right > left
        # if right > left, we need to decrease right
        # otherwise, we need to decrease just curr element

        # O(n) time O(1) space

        modify = False

        for i in range(len(nums)):
            right = nums[i+1] if i+1 < len( nums) else inf
            left = nums[i-1] if i-1 >= 0 else -inf
            if nums[i] > right:
                if modify:
                    return False
                if right < left:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = right
                modify = True


        return True 
