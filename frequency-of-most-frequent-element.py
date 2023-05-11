class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # this is a classic sliding window problem, but its kinda tricky
        # we are allowed to make at most k operations, aka increment things by 1 at most k times
        # and we want to return the frequency of the most frequent element after at most k operations
        # our friend the prefix sum comes into play here, as does sliding window
        # take this example: nums = [1,4,8,13], k = 5
        # we create a sliding window based on this condition: nums[i] * windowLen <= k + prefixSumOfWindow
            # lets break this down
            # nums[i] * windowLen gives us the prefixSum of the current window if we change everything in that window to nums[i]
                # so lets pretend L is at 1 and R is at 8
                # nums[i] * windowLen = 24, aka 8 + 8 + 8
            # prefixSumOfWindow tells us what the actual sum is so far without any changes
                # aka 1 + 4 + 8 = 13
            # prefixSumOfWindow + k tells us what that sum will be after making k operations
                # aka 13 + 5 = 18
                # aka for that L to R window, the actual sum is 13, and if we do 5 operations, it will be 18
            # so by doing nums[i] * windowLen <= k + prefixSumOfWindow, we're checking if we change eveything so far to currNum, will be go over the max number our current window can be, based on what k is
            # and if the answer to that is no, that means we can keep expanding that window
            # if the answer is yes, its time to shift our window (pop from left, expand to right)
            # also this algo only works with a sorted input
            # O(nlogn) time O(n) space

        nums.sort()

        left, right = 0, 0
        totalSum, freq = 0, 0

        while right < len(nums):
            totalSum += nums[right]
            if nums[right] * (right-left+1) <= totalSum + k:
                freq = max(freq, right-left+1)
            else:
                totalSum -= nums[left]
                left+=1
            right+=1

        return freq
