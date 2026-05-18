class TimeMap:

    def __init__(self):
        self.defaultdict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.defaultdict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.defaultdict[key]
        left = 0
        right = len(values) - 1
        result = ""
        while left <= right:
            mid = (right + left) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1 
            elif values[mid][0] > timestamp:
                right = mid - 1
        return result



        
