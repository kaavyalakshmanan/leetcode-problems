class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # O(n) time O(1) space
        # One pass
        
        output, currBuy = 0, prices[0]
        for i in range(1, len(prices)):
            output = max(output, prices[i] - currBuy)
            currBuy = min(currBuy, prices[i])
        return output 
