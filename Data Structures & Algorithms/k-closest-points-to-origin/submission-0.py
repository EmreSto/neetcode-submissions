class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []
        for x, y in points:
            distance = x*x + y*y
            pairs.append((distance , [x , y]))
        pairs.sort()
        result = []
        for pair in pairs[:k]:
            result.append(pair[1])
        return result







        