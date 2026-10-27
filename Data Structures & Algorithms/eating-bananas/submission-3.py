class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        result = high
        while low <= high:
            k = (high+low) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                result = k
                high = k - 1
            else:
                low = k + 1
        return result
        
        