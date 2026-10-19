class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
            profit_today = prices[i]- cheapest_price
            if profit_today > profit:
                profit = profit_today
        return profit







