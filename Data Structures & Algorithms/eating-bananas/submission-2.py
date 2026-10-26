class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest = 1
        highest_rate = max(piles)
        result = highest_rate
        while lowest <= highest_rate:
            k = (lowest+highest_rate) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/k)
            if total_hours <= h:
                result = k
                highest_rate = k-1
            else:
                lowest = k + 1
        return result

        