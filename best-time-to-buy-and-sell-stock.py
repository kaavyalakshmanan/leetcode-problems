class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) time O(1) space
        # Sliding window

        res = 0
        currBuy = prices[0]

        for i in range(1, len(prices)):
            currSell = prices[i]
            res = max(res, currSell - currBuy)
            currBuy = min(currBuy, currSell)

        return res
        
