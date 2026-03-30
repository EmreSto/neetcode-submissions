class Solution:
        def lastStoneWeight(self, stones: List[int]) -> int:
            heap =[]
            for stone in stones:
                heapq.heappush(heap, -stone)
            while len(heap) >= 2:
                first = -heapq.heappop(heap)
                second = -heapq.heappop(heap)
                if first != second:
                    heapq.heappush(heap, -(first-second))
            if len(heap) > 0:
                return -heap[0]
            else:
                return 0





        