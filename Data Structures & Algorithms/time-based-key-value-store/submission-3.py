class TimeMap:

    def __init__(self):
        self.my_dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = [(value,timestamp)]
        else:
            self.my_dict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        L=0
        if key not in self.my_dict:
            return ""
        R= len(self.my_dict[key])-1
        result = ""
        while L<=R:
            mid = (L+R) // 2
            value, ts = self.my_dict[key][mid]
            if ts <= timestamp:
                result = value
                L = mid + 1
            else:
                R = mid -1 
        return result
    



        
