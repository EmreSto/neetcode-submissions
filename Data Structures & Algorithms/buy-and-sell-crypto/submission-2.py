class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest_day = prices[0]
        for i in range(len(prices)):
            if prices[i] < cheapest_day:
                cheapest_day = prices[i]
            profit_today = prices[i]- cheapest_day
            if profit_today > profit:
                profit = profit_today
        return profit







