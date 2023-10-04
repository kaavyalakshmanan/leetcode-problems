class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) time O(1) space
        # Sliding window
        
        res, right = 0, 1
        minBuy = prices[0]

        while right < len(prices):
            res = max(res, prices[right] - minBuy)
            minBuy = min(minBuy, prices[right])
            right+=1


        return res
