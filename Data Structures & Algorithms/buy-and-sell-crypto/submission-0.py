class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0
        
        for i in range(len(prices)):
            sell = prices[i]
            
            if i > 0:
                
                buy = min(prices[i - 1], buy)
                diff = sell - buy
                best = max(diff, best)
        
        return best
            
                