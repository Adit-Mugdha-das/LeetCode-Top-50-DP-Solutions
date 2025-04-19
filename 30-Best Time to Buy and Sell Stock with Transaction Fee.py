class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit=0
        buy=prices[0]
        for r in prices:
            if r-fee-buy>0:
                profit+=r-fee-buy
                buy=r-fee
            buy=min(buy,r)
        return profit
    
'''SOLVED BY ADIT MUGDHA DAS'''