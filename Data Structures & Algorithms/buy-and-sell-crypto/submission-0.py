class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0
        for R in range(len(prices)):
            max_profit = max(prices[R]-prices[L], max_profit)
            
            while prices[R]< prices[L]:
                L+=1
        
        return max_profit