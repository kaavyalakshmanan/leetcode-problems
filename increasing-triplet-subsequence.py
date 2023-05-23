class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # We have to return True if we find a subsequence where for 
        # i, j, k --> i < j < k and nums[i] < nums[j] < nums[k]
        # return False otherwise
        # And this is a subsequence, not a subarray, meaning doesnt have to be
        # contiguous

        # Intuition:
        # we want to keep track of eligible firstNum and secondNum (aka) nums[i], nums[j]
        # and then find the appropriate thirdNum

        # O(n) time O(1) space

        firstNum, secondNum = inf, inf

        for n in nums:
            if n <= firstNum:
                firstNum = n
            elif n <= secondNum:
                secondNum = n
            else:
                return True

        return False
