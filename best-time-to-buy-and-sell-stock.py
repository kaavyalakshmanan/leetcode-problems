class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) time O(1) space
        # 2 pointers
        
        minSoFar = prices[0]
        maxProfit = 0

        left, right = 0, 1
        while right < len(prices):
            maxProfit = max(maxProfit, prices[right] - prices[left])
            minSoFar = min(minSoFar, prices[right])
            left = right if minSoFar < prices[left] else left
            if (prices[right] < minSoFar):
                left = right
                minSoFar = prices[right]
            right+=1

        return maxProfit

        return maxProfit
