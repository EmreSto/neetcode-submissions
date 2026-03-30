class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = 100
        for i in prices:
            if minprice > i:
                minprice = i
            if i - minprice > maxprofit:
                maxprofit = i - minprice
        return maxprofit
