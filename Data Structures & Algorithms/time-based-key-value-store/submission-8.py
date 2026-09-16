class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        t_list = self.store.get(key,[])       
        l = 0
        r = len(t_list) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if timestamp >= t_list[mid][1]:  
                res = t_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
            
        


