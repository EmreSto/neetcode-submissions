class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_n = sorted(count, key=count.get, reverse=True)
        return list(sorted_n[:k])


        