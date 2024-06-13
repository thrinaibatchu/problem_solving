class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices[1:]:
            if sell > buy:
                #do something to find the possible profit
                profit = max(profit, sell-buy) 
            
            else:
                #If sell < buy we do want this situation hence we change the buying point
                buy = sell

        return profit