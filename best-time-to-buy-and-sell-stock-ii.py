class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) time O(1) space
        # This problem is similar to Best Time to Buy and Sell Stock I, only the difference is we can buy and sell as many times as we want
        # The way to solve this is to compare a given price to the price on the left
        # If the price is greater than the price on the left, we could buy on the left and sell on the current
        # We keep doing this and accumulate and return the sum

        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += (prices[i] - prices[i-1])

        return res
