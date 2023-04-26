class Solution:
    def rob(self, nums: List[int]) -> int:

        # O(n) time O(1) space
        # this is a classic dynamic programming question, how do we recognize that?
        # in order to figure out the max amt we can rob at idx i, we need to figure out the max we can rob at idx i-1 and i-2
            # aka, since we cant rob adjacent houses, we either continue to rob from idx i-1, meaning we dont take i, or we disregard i-1 and add i-2 to i

        first, second = 0, 0
        for num in nums:
            curr = max(num + first, second)
            first = second
            second = curr

        return second
