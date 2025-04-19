class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy1,sell1=float('inf'),0
        buy2,sell2=float('inf'),0
        for p in prices:
            buy1=min(buy1,p) 
            sell1=max(sell1,p-buy1)  
            buy2=min(buy2,p-sell1)   
            sell2=max(sell2,p-buy2)  

        return sell2

'''SOLVED BY ADIT MUGDHA DAS'''