class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        way1 = cost[0]
        way2 = cost[1]
        cheapest_cost = 0
        for i in range(2, len(cost)):
            cheapest_cost = cost[i] + min(way1,way2)
            way1 = way2
            way2 = cheapest_cost
        return min(way1,way2)
            
