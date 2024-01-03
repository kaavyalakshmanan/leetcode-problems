class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) time O(1) space
        # Sliding window
        
        currSell = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - currSell)
            currSell = min(currSell, prices[i])

        return res
