class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) time O(1) space

        res = 0
        sell = prices[-1]

        for i in range(len(prices)-2, -1, -1):
            currProfit = sell - prices[i]
            res = max(res, currProfit)

            sell = max(sell, prices[i])

        return res if res > 0 else 0

