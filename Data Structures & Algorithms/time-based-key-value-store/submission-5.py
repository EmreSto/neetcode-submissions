class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = [(value,timestamp)]
        else:
            self.time_dict[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        L = 0
        if key not in self.time_dict:
            return ""
        R = len(self.time_dict[key])-1
        while L <= R:
            mid = (L+R) // 2 
            value,t = self.time_dict[key][mid]
            if t <= timestamp:
                result = value 
                L = mid + 1 
            else:
                R = mid - 1
        return result
                

            

        
