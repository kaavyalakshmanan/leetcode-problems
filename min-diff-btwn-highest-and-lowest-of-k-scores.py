class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        # lets sort input array because our chances pof minimizing are higher if we choose scores that are close to each other
        # O(nlogn) time O(n) space because sorting input array


        nums.sort()
        left, right = 0, k-1
        diff = inf

        while right < len(nums):
            currDiff = nums[right] - nums[left]
            diff = min(diff, currDiff)
            left+=1
            right+=1

        return diff
            
